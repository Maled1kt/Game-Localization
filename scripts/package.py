"""Build the upload archives from the shared Game Localization source."""

import json
from pathlib import Path
import re
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "game-localization"
CHATGPT = ROOT / "packaging" / "chatgpt"
PACKAGES = ROOT / "packages"


def write_archive(output, entries):
    temporary = output.with_suffix(".zip.tmp")
    with ZipFile(temporary, "w") as archive:
        for name, source in sorted(entries.items()):
            entry = ZipInfo(name)
            entry.compress_type = ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, source.read_bytes())
    temporary.replace(output)
    print(output.relative_to(ROOT).as_posix())


def main():
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
        SKILL / "scripts" / "update_xlsx.py",
        *(first_run / file for file in ("README.md", "source.csv", "draft.de-DE.csv", "glossary.md")),
        *sorted((SKILL / "references").rglob("*.md")),
    ]
    shared_entries = {
        f"{name}/{file.relative_to(SKILL).as_posix()}": file for file in shared_files
    }
    license_file = ROOT / "LICENSE"
    skill_license_file = SKILL / "LICENSE"
    if license_file.read_bytes() != skill_license_file.read_bytes():
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

    PACKAGES.mkdir(exist_ok=True)
    write_archive(PACKAGES / f"{name}-chatgpt-v{version}.zip", chatgpt_entries)
    write_archive(PACKAGES / f"{name}-skill-v{version}.zip", standalone_entries)


if __name__ == "__main__":
    main()
