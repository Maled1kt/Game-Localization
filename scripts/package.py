"""Build the plugin catalog bundle and both upload archives."""

import argparse
import json
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "game-localization"
CHATGPT = ROOT / "packaging" / "chatgpt"
PACKAGES = ROOT / "packages"


def package_bytes(path):
    content = path.read_bytes()
    if path.suffix in (".csv", ".json", ".md", ".py", ".yaml") or path.name == "LICENSE":
        return content.replace(b"\r\n", b"\n")
    return content


def write_archive(output, entries, *, check):
    if check:
        with ZipFile(output) as archive:
            if archive.namelist() != sorted(entries) or any(
                archive.read(name) != package_bytes(source) for name, source in entries.items()
            ):
                raise ValueError(f"Outdated archive: {output.relative_to(ROOT)}")
        return
    temporary = output.with_suffix(".zip.tmp")
    with ZipFile(temporary, "w") as archive:
        for name, source in sorted(entries.items()):
            entry = ZipInfo(name)
            entry.compress_type = ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, package_bytes(source))
    temporary.replace(output)
    print(output.relative_to(ROOT).as_posix())


def sync_catalog(entries, manifest, *, check):
    catalog = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    plugins = catalog["plugins"]
    source = "./" + CHATGPT.relative_to(ROOT).as_posix()
    if len(plugins) != 1 or plugins[0]["name"] != manifest["name"] or plugins[0]["source"] != source:
        raise ValueError("The catalog must point to the packaged Game Localization plugin.")

    files = {name: package_bytes(path) for name, path in entries.items()
             if name.startswith("skills/") or name == "LICENSE"}
    claude = {key: manifest[key] for key in ("name", "version", "description", "author", "license")}
    files[".claude-plugin/plugin.json"] = (json.dumps(claude, indent=2) + "\n").encode("utf-8")
    for name, content in files.items():
        path = CHATGPT / name
        if path.is_file() and path.read_bytes() == content:
            continue
        if check:
            raise ValueError(f"Outdated catalog file: {path.relative_to(ROOT)}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)

    skill_root = CHATGPT / "skills"
    for path in sorted(skill_root.rglob("*")):
        if path.is_file() and path.relative_to(CHATGPT).as_posix() not in files:
            if check or not path.resolve().is_relative_to(skill_root.resolve()):
                raise ValueError(f"Unexpected catalog file: {path.relative_to(ROOT)}")
            path.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check the existing bundle and ZIPs without writing")
    args = parser.parse_args()
    manifest_file = CHATGPT / ".codex-plugin" / "plugin.json"
    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    name, version = manifest["name"], manifest["version"]
    if name != SKILL.name or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("The plugin name or release version is invalid.")

    first_run = SKILL / "examples" / "first-run"
    shared_files = [
        SKILL / "SKILL.md",
        SKILL / "scripts" / "check_csv.py",
        SKILL / "scripts" / "estimate_ui_width.py",
        SKILL / "scripts" / "prepare_csv_update.py",
        SKILL / "scripts" / "prepare_steam_store.py",
        SKILL / "scripts" / "update_xlsx.py",
        *(first_run / file for file in ("README.md", "source.csv", "draft.de-DE.csv", "glossary.md")),
        *sorted((SKILL / "references").rglob("*.md")),
    ]
    shared_entries = {
        f"{name}/{file.relative_to(SKILL).as_posix()}": file for file in shared_files
    }
    license_file = ROOT / "LICENSE"
    skill_license_file = SKILL / "LICENSE"
    if package_bytes(license_file) != package_bytes(skill_license_file):
        raise ValueError("The repository and skill license notices must match.")
    standalone_entries = {**shared_entries, f"{name}/LICENSE": skill_license_file}
    chatgpt_entries = {
        f"skills/{entry}": file for entry, file in shared_entries.items()
    }
    chatgpt_entries["LICENSE"] = license_file
    chatgpt_entries[f"skills/{name}/agents/openai.yaml"] = SKILL / "agents" / "openai.yaml"
    chatgpt_entries[".codex-plugin/plugin.json"] = manifest_file
    for key in ("logo", "composerIcon"):
        asset = manifest["interface"][key]
        if not asset.startswith("./assets/") or ".." in Path(asset).parts:
            raise ValueError(f"Invalid path for plugin {key}.")
        chatgpt_entries[asset.removeprefix("./")] = CHATGPT / asset

    sync_catalog(chatgpt_entries, manifest, check=args.check)
    if not args.check:
        PACKAGES.mkdir(exist_ok=True)
    write_archive(PACKAGES / f"{name}-chatgpt-v{version}.zip", chatgpt_entries, check=args.check)
    write_archive(PACKAGES / f"{name}-skill-v{version}.zip", standalone_entries, check=args.check)


if __name__ == "__main__":
    main()
