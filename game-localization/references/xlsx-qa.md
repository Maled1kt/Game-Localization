# Excel translation and verification

Use this workflow when the deliverable is a translated copy of an existing `.xlsx` workbook.

1. Identify the worksheet, header row, stable row ID column, source column, and existing target column. Confirm any detail the brief or workbook leaves ambiguous. The source and target columns must be different. If the user requests more than one worksheet or target column, check each pass separately and use the last verified copy as the input to the next pass.
2. Read the relevant source, IDs, and context without editing the workbook. Draft the requested translations and check meaning, terminology, placeholders, tags, and limits. For the supported technical checks, use the [CSV checker](csv-qa.md) with a source export covering the same selected IDs.
3. Write a temporary UTF-8 comma-separated CSV with exactly two headers, `ID,TRANSLATION`. Include one row per translation to write. Match IDs exactly, even when the CSV is in a different order. Preserve leading zeros in text IDs. Quote cells with commas, quotes, or line breaks. Leave unresolved rows out of the write batch and record their IDs in the handoff.
4. Run the [workbook updater](../scripts/update_xlsx.py) from the skill folder with Python 3.9 or later. This example writes to the existing `GERMAN` column on the `Strings` worksheet. Add `--header-row 3` if the headers are on row 3.

```sh
python scripts/update_xlsx.py source.xlsx translations.csv translated.xlsx --sheet Strings --id-column ID --target-column GERMAN
```

5. Use the JSON report to check the worksheet and the exact cell addresses written. The updater reads back the saved text and existing target cell styles, compares the rest of the worksheet, and verifies that the other archive parts are unchanged except for any required additions to the shared string table. Existing shared strings keep their values and positions. Return the new workbook and a [separate handoff](handoff.md). Report what passed, omitted IDs, and any app, formula recalculation, language, or in-game checks still pending.

The updater supports ordinary, unsigned `.xlsx` workbooks with one exact worksheet name and plain-text headers. It can fill blank cells or replace plain text, including Excel's shared strings. IDs must be unique literal text or numbers. Numeric IDs match the workbook's stored value. Use text IDs when the visible form includes leading zeros or other formatting. Targets containing formulas, intersecting a formula range or merged cell, carrying cell metadata, or containing rich text or non-text values are outside this workflow. A protected worksheet, unknown or duplicate ID, unsupported input, or existing output path stops the update without replacing either file. For a row with no stored target cell, the new cell uses the worksheet's normal defaults.

When the runtime cannot run the updater, or the workbook is outside its supported scope, describe the specific limitation and offer a reviewed CSV keyed by ID for the user to import. Mark Excel preservation as pending unless the output workbook was verified.
