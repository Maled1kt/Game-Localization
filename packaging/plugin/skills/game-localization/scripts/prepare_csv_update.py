"""Prepare a translation update from two complete CSV source revisions."""

import argparse
from collections import Counter
import csv
import json
from pathlib import Path

from check_csv import compare_text, read_table


def load_rows(path, delimiter, id_column, columns):
    try:
        rows, _, issues = read_table(path, delimiter, id_column, columns)
    except (OSError, ValueError, csv.Error) as error:
        raise ValueError(f"{path}: {error}") from error
    if issues:
        issue = issues[0]
        problem = f"Duplicate ID {issue['id']!r}" if issue["code"] == "duplicate_id" else "Blank ID"
        raise ValueError(f"{path}: {problem} at record {issue['record']}.")
    return rows


def check_target_ids(path, rows, allowed_ids):
    unexpected = rows.keys() - allowed_ids
    if unexpected:
        raise ValueError(f"{path}: Unexpected translation IDs: {', '.join(sorted(unexpected))}.")


def classify_rows(previous, current, accepted, editor, args):
    draft_rows = []
    changes = []
    scenes = {}
    columns = dict.fromkeys((args.source_column, *args.compare_column))
    if args.scene_column is not None:
        columns[args.scene_column] = None

    # Keep the current export's order. List deleted IDs afterwards in their old order.
    for row_id in dict.fromkeys((*current, *previous)):
        old = previous.get(row_id)
        new = current.get(row_id)
        prior_text = accepted[row_id][args.target_column] if row_id in accepted else None
        editor_text = editor[row_id][args.target_column] if row_id in editor else None
        preferred = editor_text if editor_text is not None else prior_text
        entry = {"id": row_id}
        if new is None:
            entry.update(change="removed", status="removed")
        elif old is None:
            entry.update(change="added", status="needs_review", reason="new_source")
        else:
            differences = {
                column: {"previous": old[column], "current": new[column]}
                for column in columns if old[column] != new[column]
            }
            if differences:
                entry.update(change="modified", status="needs_review", reason="changed_source",
                             changed_columns=differences)
            else:
                entry["change"] = "unchanged"
                if preferred is None or not preferred.strip():
                    reason = "blank_editor_translation" if editor_text is not None else "missing_translation"
                    entry.update(status="needs_review", reason=reason)
                elif issues := compare_text(new[args.source_column], preferred):
                    entry.update(status="needs_review", reason="technical_issues", issues=issues)
                else:
                    status = "preserved_editor" if editor_text is not None and editor_text != prior_text else "reused"
                    entry["status"] = status

        if entry["status"] in ("needs_review", "removed"):
            if prior_text is not None:
                entry["prior_translation"] = prior_text
            if editor_text is not None:
                entry["editor_translation"] = editor_text
        if new is not None:
            text = preferred if entry["status"] in ("reused", "preserved_editor") else ""
            draft_rows.append((row_id, text))

        if args.scene_column is not None:
            scene = (new if new is not None else old)[args.scene_column]
            entry["scene"] = scene
            group = scenes.setdefault(scene, {"scene": scene, "review_ids": [], "removed_ids": []})
            if entry["status"] == "needs_review":
                group["review_ids"].append(row_id)
            elif entry["status"] == "removed":
                group["removed_ids"].append(row_id)
        changes.append(entry)

    return draft_rows, {
        "status": "needs_review" if any(row["status"] == "needs_review" for row in changes) else "prepared",
        "source_changes": dict(Counter(row["change"] for row in changes)),
        "translation_statuses": dict(Counter(row["status"] for row in changes)),
        "rows": changes,
        "scenes": list(scenes.values()),
    }


def write_draft(path, headers, rows, delimiter):
    # Exclusive creation protects input files and prior drafts, including concurrent runs.
    file = path.open("x", encoding="utf-8", newline="")
    try:
        with file:
            writer = csv.writer(file, delimiter=delimiter)
            writer.writerow(headers)
            writer.writerows(rows)
    except BaseException:
        path.unlink()
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("previous_source", type=Path)
    parser.add_argument("current_source", type=Path)
    parser.add_argument("accepted_translation", type=Path)
    parser.add_argument("output", type=Path, help="New working CSV path")
    parser.add_argument("--editor", type=Path, help="Optional CSV containing intentional editor changes")
    parser.add_argument("--id-column", required=True)
    parser.add_argument("--source-column", required=True)
    parser.add_argument("--target-column", required=True)
    parser.add_argument("--compare-column", action="append", default=[], help="Extra source field to compare")
    parser.add_argument("--scene-column", help="Source field used for scene grouping and change detection")
    parser.add_argument("--delimiter", choices=("comma", "semicolon", "tab"), default="comma")
    args = parser.parse_args()

    source_columns = [args.source_column, *args.compare_column]
    if args.scene_column is not None:
        source_columns.append(args.scene_column)
    if args.id_column in (*source_columns, args.target_column):
        parser.error("Use a separate ID column.")
    delimiter = {"comma": ",", "semicolon": ";", "tab": "\t"}[args.delimiter]
    try:
        previous = load_rows(args.previous_source, delimiter, args.id_column, source_columns)
        current = load_rows(args.current_source, delimiter, args.id_column, source_columns)
        accepted = load_rows(args.accepted_translation, delimiter, args.id_column, [args.target_column])
        check_target_ids(args.accepted_translation, accepted, previous.keys())
        editor = {}
        if args.editor is not None:
            editor = load_rows(args.editor, delimiter, args.id_column, [args.target_column])
            check_target_ids(args.editor, editor, previous.keys() | current.keys())
        rows, report = classify_rows(previous, current, accepted, editor, args)
        write_draft(args.output, (args.id_column, args.target_column), rows, delimiter)
    except (OSError, ValueError, csv.Error) as error:
        parser.exit(2, f"Could not prepare CSV update: {error}\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
