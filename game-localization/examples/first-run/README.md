# First run with Game Localization

Review a German (`de-DE`) draft of 12 English strings for a fictional space station game. The example shows how the skill fixes technical problems, asks about unclear wording, and reports the result separately from the CSV.

## Run it in your app

1. Install Game Localization from the package for your app. The plugin and standalone ZIPs include these sample files under `examples/first-run/` inside the skill folder.
2. Download or extract [source.csv](source.csv), [draft.de-DE.csv](draft.de-DE.csv), and [glossary.md](glossary.md).
3. Start a new chat, select Game Localization, attach the three files, and send the prompt below. If the skill already has access to its bundled example, you can ask it to use those files.

```text
Use Game Localization to review the attached German (de-DE) draft against the English source for this fictional game.
Match the files by ID. Use ENGLISH and CONTEXT in source.csv, GERMAN in draft.de-DE.csv, and the approved terms in glossary.md.
Use each nonblank MAX_LENGTH value as a limit in characters. Preserve the IDs, placeholders, tags, and the ID,GERMAN schema.
Fix the rows with clear corrections. If a row needs a decision about meaning, keep its ID and leave the translation blank in the labeled draft. Ask me about it by ID.
Return a new CSV called reviewed.de-DE.draft.csv and a separate handoff in English. Run the CSV checker if available. The game build is unavailable.
Include an in-build checklist. The docking area supports the Interact binding Umschalt + Eingabe. Use it to plan a check of the airlock prompt.
```

## What to expect

The original draft has two fixable problems and one unresolved row. A reviewed copy should keep all 12 IDs, translate 11 rows, and leave `MENU_006` blank until you clarify the action.

| ID | What the review should do |
| --- | --- |
| `MENU_001` | Keep the valid translation `Neues Spiel`. |
| `MENU_005` | Replace the 10-character `Fortfahren` with a suitable label of 8 characters or fewer. `Weiter` uses 6 characters and fits the next-step action. |
| `TUT_014` | Restore `{interact}` and use the approved term `Luftschleuse`. One option is `Halte {interact} gedrückt, um die Luftschleuse zu öffnen`. |
| `MENU_006` | Ask what `Clear` does before translating it. |

The wording of the handoff can vary. It should give the same decisions and report what was actually checked. Here is an example when the CSV checker is available.

> **Draft for review.** `reviewed.de-DE.draft.csv` contains 12 IDs and 11 translations. Confirm `MENU_006` before importing the complete file.
>
> - **File checks need action.** The checker compared all 12 IDs. `{interact}` was restored in `TUT_014` and `MENU_005` now fits the 8-character limit. `MENU_006` is the only remaining blank translation.
> - **Language review needs action.** The approved glossary was applied to the translated rows. Does `MENU_006` clear filters, delete a save, or do something else?
> - **In-game review pending.** In `de-DE`, bind Interact to `Umschalt + Eingabe` and approach the closed airlock in the docking area at the highest supported text scale. For `TUT_014`, verify that the whole binding and instruction are visible without clipping. For `MENU_005`, open the tutorial's next step at the narrowest supported viewport and check that `Weiter` appears in full inside the button. Width estimates need the font and usable width.

See the [in-build checklist](../../references/in-build-qa.md) for the same checks as a table.

To finish the example, reply with `MENU_006 clears the active filters. Update that row and rerun the checks.` A suitable translation is `Filter zurücksetzen`. The file can pass technical checks once that row is filled. In-game review still needs a build.

## Run the technical check locally

From this example folder, run the command below with Python 3.9 or later. The supplied draft returns three findings. After reviewing a copy, substitute its filename for `draft.de-DE.csv`.

```text
python ../../scripts/check_csv.py source.csv draft.de-DE.csv --id-column ID --source-column ENGLISH --target-column GERMAN --limit-column MAX_LENGTH --limit-unit characters
```
