# CSV technical QA

Run [the CSV checker](../scripts/check_csv.py) on the source and the actual target deliverable before handoff. Use the exact headers and delimiter for the project. The checker reads both files and prints a JSON report to standard output.

```text
python scripts/check_csv.py source.csv translated.csv --id-column ID --source-column ENGLISH --target-column RUSSIAN
```

Resolve `scripts/check_csv.py` relative to the skill folder. The checker uses Python 3.9 or later and the standard library. It accepts UTF-8 with or without a BOM. It reads comma-separated files by default. Set `--delimiter semicolon` or `--delimiter tab` if needed. Use the same ID header and delimiter in both files. The source and target text headers may differ. You can also supply the same file twice when checking two columns in one export.

- Use `--limit 24 --limit-unit characters` for one maximum or `--limit-column MAX_LENGTH --limit-unit characters` for a column of maximums in the source CSV. Blank limits in that column mean no maximum for the row. Use `utf8-bytes` for a UTF-8 byte limit. `characters` counts Unicode code points. Both measure the raw target cell, including markup and placeholder spelling. Check rendered limits and other units separately according to the brief.
- The checker compares ID coverage, flags blank or duplicate IDs and empty translations for nonblank source strings, and matches the exact spelling and counts of simple `{name}` or `{0}` placeholders, doubled braces, common printf conversions such as `%s`, `%02d`, `%1$s` and `%%`, and angle-bracket tags such as `<b>` and `<color=#fff>`. It also checks the order of unnumbered printf conversions and the tag sequence.
- Verify project-specific syntax, placeholder binding and scope, significant line breaks, and other schema constraints separately. A passing script report covers only the checks above. Use the project rules for additional technical, language, and build checks.
- Exit `0` means the script checks passed. Exit `1` means it found row issues. Exit `2` means an input or argument error prevented a complete check. In the JSON report, use `issues` to identify affected IDs, record numbers or files. Correct recoverable issues and rerun the checker. Keep unresolved errors in the separate handoff and label the affected output as draft.
- If the script cannot run or a file lacks stable IDs, use the available format-aware or manual checks. Report the method, what was actually checked, and what is pending.

For example, if `{interact}` disappears from the translation of `TUT_014`, the `issues` array contains this entry.

```json
{
  "id": "TUT_014",
  "code": "protected_tokens",
  "missing": {"{interact}": 1},
  "unexpected": {}
}
```
