# Update a translation by ID

Use this workflow when a game already has translations and the source CSV has changed. Work on one target locale per run.

## Prepare the update

1. Get the complete previous and current source exports, the accepted target export for the previous revision, and any later editor changes. Use the same stable ID header in every file. Match IDs exactly and keep leading zeros. Compare two complete exports of the same scope so an omitted row can be identified as removed.
2. Include every source field that could affect the translation. Use `--compare-column` for fields such as context, speaker, or a character limit. Use `--scene-column` to group dialogue by scene and detect scene changes. Columns without a comparison option are ignored, and a change in row order alone does not require retranslation.
3. Run the [CSV update helper](../scripts/prepare_csv_update.py) with Python 3.9 or later from the skill folder. Use UTF-8 inputs with or without a BOM. All files use the same delimiter. Set `--delimiter semicolon` or `--delimiter tab` as needed. Use a new path for the working CSV and a separate new path for the report.

```sh
python -B scripts/prepare_csv_update.py old.csv current.csv accepted.de-DE.csv update.de-DE.draft.csv --editor editor.de-DE.csv --id-column ID --source-column ENGLISH --target-column GERMAN --compare-column CONTEXT --scene-column SCENE > update-report.json
```

The accepted export contains the latest approved target text against the previous source. The optional editor CSV contains the intended overrides and can list only the edited IDs. Omit `--editor` if there are none. A blank editor value is an explicit empty edit and goes to review. An ID absent from the editor CSV retains its accepted value. Input files and existing working CSVs are protected from overwrite.

## Read the report and review the draft

| Source change | What the draft and report contain |
| --- | --- |
| Unchanged | The working CSV keeps the latest editor wording if supplied. Otherwise it keeps the accepted translation. A missing or blank translation or a supported placeholder or tag issue leaves the row blank for review. |
| Added | The working CSV includes the ID with a blank translation. Any editor wording appears in the report for review. |
| Modified | The working CSV includes the ID with a blank translation. The report shows which source fields changed and keeps both accepted and editor wording when supplied. Compare them before choosing or rewriting a translation. |
| Removed | The report keeps the ID and its existing wording for reference. The working CSV omits the row. Report the removal separately if the game imports changes incrementally. |

The working CSV contains the ID and target columns in current source order. Keep it separate from the JSON report. A successful command prepares the draft even when rows remain open. Exit `2` means the inputs or output path prevented preparation. A repeated ID, blank ID, unknown target ID, or malformed input stops the update. An accepted ID must exist in the old source. An editor ID can exist in either revision.

Give the user counts for new, modified, removed, reused, and preserved editor rows. Identify open decisions by ID. Resolve changed strings against the current glossary and brief. If both the source and the editor's wording changed, keep the editor wording available and flag any conflict before replacing it. Run the [CSV checker](csv-qa.md) against the current source and the working translation, including any configured length limits. Keep the deliverable labeled as draft while unresolved IDs or other blockers remain. Follow the [handoff guide](handoff.md) for separate file, language, and build checks.

## Save progress by scene

For a large dialogue batch, take one scene at a time. Use the report's `scenes` list to find the scene's review IDs and removed IDs. A moved ID belongs to its current scene and needs review. A removed ID remains listed under its former scene. If a row has no scene, group it as unassigned until the project supplies one.

After each scene, save a new working CSV and return a separate checkpoint with the target locale, exact source revision, glossary version, latest working CSV, and comparison report. Use a source file checksum if the export has no revision identifier. Record reviewed and pending IDs by scene, plus any decision the next reviewer needs. Save completed wording in the working CSV. Keep the checkpoint outside the import file.

```markdown
# Dialogue checkpoint

- Locale — de-DE
- Source revision — station-dialogue-v2 (current.csv)
- Glossary — station-glossary-v3.md
- Working translation — update.de-DE.scene-01.draft.csv
- Comparison report — update-report.json

| Scene | Reviewed IDs | Pending IDs | Next action |
| --- | --- | --- | --- |
| Docking | DIA_001 | DIA_002 | Confirm which door the line refers to. |
| Control room | | DIA_004 | Review the new line against the glossary. |
```

In a new chat, attach the checkpoint, the files it names, and the current glossary. Check the locale and source revision. Use the latest working CSV as the starting point and continue at the next pending ID. Carry forward reviewed wording and editor decisions. If the source revision changed, use the checkpoint's source as the previous source and the accepted rows from the working CSV as the baseline translations. Retain unresolved editor wording for the new review.

## Try the example

Save these four UTF-8 CSV files and run the command above.

**`old.csv`**

```csv
ID,ENGLISH,SCENE,CONTEXT
DIA_001,Stay close.,Docking,Teammate
MENU_001,New Game,,Menu
DIA_002,Open the airlock.,Docking,Teammate
DIA_003,Go to the bridge.,Bridge,Teammate
```

**`current.csv`**

```csv
ID,ENGLISH,SCENE,CONTEXT
MENU_001,New Game,,Menu
DIA_001,Stay close.,Docking,Teammate
DIA_002,Close the airlock.,Docking,Teammate
DIA_004,Check the controls.,Control room,Teammate
```

**`accepted.de-DE.csv`**

```csv
ID,GERMAN
DIA_001,Bleib bei mir.
DIA_002,Öffne die Luftschleuse.
DIA_003,Geh zur Brücke.
MENU_001,Neues Spiel
```

**`editor.de-DE.csv`**

```csv
ID,GERMAN
DIA_001,Bleib dicht bei mir.
DIA_002,Mach die Luftschleuse auf.
```

The draft keeps `Neues Spiel` for `MENU_001` and the editor's `Bleib dicht bei mir.` for `DIA_001`. The revised `DIA_002` asks the player to close the airlock, so its cell stays blank and both old translations appear in the report. The new `DIA_004` has a blank to translate. The removed `DIA_003` appears in the report under Bridge.

Review `DIA_002` in Docking and save the working CSV and a checkpoint. Reopen them for Control room, fill `DIA_004`, and check that the two carried translations and the reviewed `DIA_002` are still present.
