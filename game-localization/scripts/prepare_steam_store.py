"""Prepare a draft translation of Steam store descriptions in a JSON export."""

import argparse
from decimal import Decimal
import json
from pathlib import Path
import re

from check_csv import compare_text, protected_tokens


FIELD_KEYS = {
    "short_description": "app[content][short_description]",
    "about": "app[content][about]",
}
BBCODE = re.compile(r"\[\*\]|\[/?[a-z][a-z0-9_]*(?:=[^\]\r\n]*)?\]", re.IGNORECASE)
BBCODE_TARGET = re.compile(r"\[(img|url)\](.*?)\[/\1\]", re.IGNORECASE | re.DOTALL)


def unique_object(pairs):
    values = {}
    for key, value in pairs:
        if key in values:
            raise ValueError(f"Duplicate JSON key {key!r}.")
        values[key] = value
    return values


def unsupported_number(value):
    raise ValueError(f"Unsupported JSON number {value!r}.")


def exact_number(value):
    number = float(value)
    if Decimal(value) != Decimal(str(number)):
        raise ValueError(f"JSON number {value!r} would lose precision.")
    return number


def read_object(path):
    with path.open(encoding="utf-8-sig") as file:
        value = json.load(file, object_pairs_hook=unique_object,
                          parse_float=exact_number, parse_constant=unsupported_number)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: Expected a JSON object.")
    return value


def language_fields(export, source, target):
    item_id = export.get("itemid")
    if type(item_id) not in (str, int) or not re.fullmatch(r"[0-9]+", str(item_id)):
        raise ValueError("Expected a numeric itemid in the store export.")
    languages = export.get("languages")
    if not isinstance(languages, dict):
        raise ValueError("Expected a multilingual store export with a languages object.")
    for language in (source, target):
        if not isinstance(languages.get(language), dict):
            raise ValueError(f"Language {language!r} must already have an object in the export.")
    return languages[source], languages[target]


def check_field(field, source, translation, limit):
    if not isinstance(source, str) or not source.strip():
        raise ValueError(f"{field}: Expected source text in the export.")
    if not isinstance(translation, str) or not translation.strip():
        raise ValueError(f"{field}: Supply nonblank translated text.")
    if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", translation):
        raise ValueError(f"{field}: Unexpected control characters.")
    if field == "short_description" and (
        translation.splitlines() != [translation] or "\t" in translation or BBCODE.search(translation)
        or any(kind == "tag" for kind, _ in protected_tokens(translation))
    ):
        raise ValueError(f"{field}: Use plain, single-line text.")
    if field == "about" and (
        BBCODE.findall(source) != BBCODE.findall(translation)
        or BBCODE_TARGET.findall(source) != BBCODE_TARGET.findall(translation)
    ):
        raise ValueError(f"{field}: BBCode or an embedded image or link target changed.")
    if issues := compare_text(source, translation):
        details = ", ".join(issue["code"] for issue in issues)
        raise ValueError(f"{field}: Protected text check failed ({details}).")

    length = len(translation)
    if limit is not None and length > limit:
        raise ValueError(f"{field}: {length} characters exceed the supplied limit of {limit}.")
    return {
        "characters": length,
        "utf8_bytes": len(translation.encode("utf-8")),
        "limit_characters": limit,
        "length_status": "passed" if limit is not None else "pending",
    }


def prepare(export, translations, args):
    source, target = language_fields(export, args.source_language, args.target_language)
    if not translations or translations.keys() - FIELD_KEYS.keys():
        raise ValueError("Use short_description, about, or both in the translation JSON.")
    limits = {"short_description": args.short_limit, "about": args.about_limit}
    checks = {}
    changes = {}
    for field, translation in translations.items():
        key = FIELD_KEYS[field]
        existing = target.get(key, "")
        if not isinstance(existing, str):
            raise ValueError(f"{field}: Expected text in the target field.")
        if existing.strip() and existing != translation and not args.replace_existing:
            raise ValueError(f"{field}: Target already contains text. Confirm replacement before using --replace-existing.")
        checks[field] = check_field(field, source.get(key), translation, limits[field])
        changes[key] = translation
    target.update(changes)
    return {
        "status": "draft",
        "itemid": export["itemid"],
        "target_language": args.target_language,
        "fields": checks,
        "steamworks_import": "pending",
    }


def write_draft(path, data):
    # Serialize first and create exclusively to protect inputs and existing drafts.
    contents = json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    contents.encode("utf-8")
    file = path.open("x", encoding="utf-8", newline="\n")
    try:
        with file:
            file.write(contents)
    except BaseException:
        path.unlink()
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("export", type=Path, help="Multilingual store localization export")
    parser.add_argument("translations", type=Path, help="JSON containing the reviewed target text by field")
    parser.add_argument("output", type=Path, help="New draft JSON path")
    parser.add_argument("--source-language", default="english", help="Exact language key in the export")
    parser.add_argument("--target-language", required=True, help="Exact target language key in the export")
    parser.add_argument("--short-limit", type=int, help="Supplied short description limit in Unicode code points")
    parser.add_argument("--about-limit", type=int, help="Supplied About This Game limit in Unicode code points")
    parser.add_argument("--replace-existing", action="store_true", help="Allow replacing populated target text in the draft")
    args = parser.parse_args()
    if args.source_language == args.target_language:
        parser.error("Choose different source and target languages.")
    if any(limit is not None and limit <= 0 for limit in (args.short_limit, args.about_limit)):
        parser.error("Length limits must be positive.")
    try:
        export = read_object(args.export)
        translations = read_object(args.translations)
        report = prepare(export, translations, args)
        write_draft(args.output, export)
    except (OSError, ValueError, RecursionError) as error:
        parser.exit(2, f"Could not prepare Steam store draft: {error}\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
