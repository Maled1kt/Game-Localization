"""Compare game localization CSV files and print a JSON report."""

import argparse
from collections import Counter
import csv
import json
from pathlib import Path
import re


PROTECTED = re.compile(
    r"(?P<tag></?[A-Za-z][\w:-]*(?=[\s=/>])(?:[^<>\"']|\"[^\"]*\"|'[^']*')*>)"
    r"|(?P<brace>\{\{|\}\}|\{(?:[A-Za-z_]\w*|[0-9]+)\})|(?P<percent>%%)"
    r"|(?P<printf>%(?P<position>[1-9][0-9]*\$)?[-+#0']*[0-9]*(?:\.[0-9]+)?"
    r"(?:hh|ll|[hljztL])?[diuoxXfFeEgGaAcspn])"
)


def read_table(path, delimiter, id_column, columns):
    rows = {}
    duplicates = set()
    issues = []
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.reader(stream, delimiter=delimiter, strict=True)
        headers = next(reader, [])
        if not headers or any(not header.strip() for header in headers):
            raise ValueError("Expected a header row with nonblank column names.")
        if len(set(headers)) != len(headers):
            raise ValueError("Column names must be unique.")
        missing = sorted({id_column, *columns} - set(headers))
        if missing:
            raise ValueError(f"Missing columns: {', '.join(missing)}.")

        for record, values in enumerate(reader, start=2):
            if not values:
                continue
            if len(values) != len(headers):
                raise ValueError(f"Record {record} has {len(values)} fields, expected {len(headers)}.")
            row = dict(zip(headers, values))
            row_id = row[id_column]
            if not row_id.strip():
                issues.append({"code": "blank_id", "record": record})
            elif row_id in rows:
                duplicates.add(row_id)
                issues.append({"code": "duplicate_id", "id": row_id, "record": record})
            else:
                rows[row_id] = row
    return rows, duplicates, issues


def protected_tokens(value):
    return [
        ("positional_printf" if match.group("position") else match.lastgroup, match.group())
        for match in PROTECTED.finditer(value)
    ]


def compare_text(source, target):
    if source.strip() and not target.strip():
        return [{"code": "empty_translation"}]

    source_tokens = protected_tokens(source)
    target_tokens = protected_tokens(target)
    source_counts = Counter(token for _, token in source_tokens)
    target_counts = Counter(token for _, token in target_tokens)
    if source_counts != target_counts:
        return [{
            "code": "protected_tokens",
            "missing": dict(source_counts - target_counts),
            "unexpected": dict(target_counts - source_counts),
        }]

    issues = []
    for kind, code in (("tag", "tag_order"), ("printf", "printf_order")):
        before = [token for group, token in source_tokens if group == kind]
        after = [token for group, token in target_tokens if group == kind]
        if before != after:
            issues.append({"code": code, "expected": before, "actual": after})
    return issues


def check_length(source_row, target, args):
    limit = args.limit
    if args.limit_column is not None:
        raw_limit = source_row[args.limit_column].strip()
        if not raw_limit:
            return None
        if not re.fullmatch(r"[0-9]+", raw_limit):
            return {"code": "invalid_limit", "value": raw_limit}
        try:
            limit = int(raw_limit)
        except ValueError:
            return {"code": "invalid_limit", "value": raw_limit}
    if limit is None:
        return None

    actual = len(target.encode("utf-8")) if args.limit_unit == "utf8-bytes" else len(target)
    if actual > limit:
        return {"code": "length_limit", "unit": args.limit_unit, "limit": limit, "actual": actual}
    return None


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path)
    parser.add_argument("--id-column", required=True, help="ID header in both files")
    parser.add_argument("--source-column", required=True)
    parser.add_argument("--target-column", required=True)
    parser.add_argument("--delimiter", choices=("comma", "semicolon", "tab"), default="comma")
    limits = parser.add_mutually_exclusive_group()
    limits.add_argument("--limit", type=int, help="Maximum length for every translation")
    limits.add_argument("--limit-column", help="Source header with per-row maximum lengths")
    parser.add_argument("--limit-unit", choices=("characters", "utf8-bytes"))
    args = parser.parse_args()
    has_limit = args.limit is not None or args.limit_column is not None
    if has_limit != (args.limit_unit is not None):
        parser.error("Supply --limit-unit together with --limit or --limit-column.")
    if args.limit is not None and args.limit < 0:
        parser.error("--limit must be nonnegative.")
    if args.id_column in (args.source_column, args.target_column, args.limit_column):
        parser.error("Use a separate ID column.")
    if args.limit_column == args.source_column:
        parser.error("Use a separate source length limit column.")
    return args


def main():
    args = parse_args()
    delimiter = {"comma": ",", "semicolon": ";", "tab": "\t"}[args.delimiter]
    source_columns = [args.source_column]
    if args.limit_column is not None:
        source_columns.append(args.limit_column)

    tables = {}
    duplicate_ids = set()
    issues = []
    for role, path, columns in (
        ("source", args.source, source_columns),
        ("target", args.target, [args.target_column]),
    ):
        try:
            rows, duplicates, row_issues = read_table(path, delimiter, args.id_column, columns)
        except (OSError, ValueError, csv.Error) as error:
            issues.append({"code": "invalid_csv", "file": role, "message": str(error)})
            continue
        tables[role] = rows
        duplicate_ids.update(duplicates)
        issues.extend({"file": role, **issue} for issue in row_issues)

    checked_rows = 0
    if len(tables) == 2:
        source = tables["source"]
        target = tables["target"]
        issues.extend({"code": "missing_id", "id": row_id} for row_id in source if row_id not in target)
        issues.extend({"code": "unexpected_id", "id": row_id} for row_id in target if row_id not in source)
        for row_id, source_row in source.items():
            if row_id not in target or row_id in duplicate_ids:
                continue
            checked_rows += 1
            target_text = target[row_id][args.target_column]
            row_issues = compare_text(source_row[args.source_column], target_text)
            length_issue = check_length(source_row, target_text, args)
            if length_issue:
                row_issues.append(length_issue)
            issues.extend({"id": row_id, **issue} for issue in row_issues)

    print(json.dumps({
        "status": "failed" if issues else "passed",
        "source_ids": len(tables["source"]) if "source" in tables else None,
        "target_ids": len(tables["target"]) if "target" in tables else None,
        "checked_rows": checked_rows,
        "issues": issues,
    }, indent=2))
    return 2 if len(tables) != 2 else int(bool(issues))


if __name__ == "__main__":
    raise SystemExit(main())
