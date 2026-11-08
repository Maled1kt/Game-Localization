# Game Localization roadmap

**Current status.** P0.2 is complete. Version `0.1.5` gives users a separate handoff with the deliverable's readiness, three review statuses, and next actions for open issues. [Handoff guide](game-localization/references/handoff.md) · [Changelog](CHANGELOG.md)

**Next task.** P0.3. Add a first-run example with a fictional CSV, glossary, prompt, and expected handoff. Try both packages in their intended apps.

To resume work in a new session, read this file and [AGENTS.md](AGENTS.md), inspect `git status`, and continue the next task. Update the status and identify the next task after verifying the work.

## P0 · Verifiable CSV translation

- [x] **P0.1. Check CSV before handoff.** Match rows by ID and flag missing, unexpected or duplicate IDs, empty translations, changes to common placeholders and tags, and length limit violations. Return a JSON report with issues by row. [Checker](game-localization/scripts/check_csv.py) · [Tests](tests/test_check_csv.py)
- [x] **P0.2. Separate the translation and handoff.** Turn CSV findings into plain-language items with the row ID, the problem, and the next action. Report file, language, and in-build checks separately. Label output as draft while an issue blocks import. [Handoff guide](game-localization/references/handoff.md)
- [ ] **P0.3. Add a first-run example.** Provide a fictional 12-row CSV, a small glossary, a prompt, and an expected handoff. Include a normal translation, a missing placeholder, a length limit, and one question about meaning. Done when users can reproduce the example from the README and both packages have been tried in their intended apps.

## P1 · Working with a real project

- [ ] **P1.1. Make the project glossary portable.** Provide a template with locale, context, and term status. Save approved decisions in a file for the next chat and list proposed terms separately.
- [ ] **P1.2. Verify Excel workbooks.** For supported `.xlsx` files, write translations to the requested column in a new copy and verify that the rest of the workbook is preserved. Then evaluate support for simple JSON resources.
- [ ] **P1.3. Give testers specific in-build checks.** Identify the screen, string ID, and conditions for each check. Start with long substitutions and clipped text. Add width estimates when font and layout parameters are available.

## P2 · Translation updates and Steam

- [ ] **P2.1. Process changes by ID.** Identify new, modified, and removed rows, reuse accepted translations, and preserve editor changes. Add scene-level checkpoints for large dialogue batches.
- [ ] **P2.2. Add a Steam store page workflow.** Return translations by field with length and fact checks. Verify the import format through a trial import using a real Steamworks export.

## Version 0.1.4 verification

- All five CSV regression tests passed. Run them with `python -B -m unittest discover -s tests -v`.
- Both ZIPs built reproducibly and passed CSV checks from their extracted contents. All local links in the 30 README editions resolved. Build the ZIPs with `python scripts/package.py`.
- App import and a trial run in each intended app are tracked under P0.3.

## Version 0.1.5 verification

- All five CSV regression tests passed. Both ZIPs rebuilt byte for byte and contained the new handoff guide and its linked references. All local links in the 30 README editions resolved.
- The checker from each extracted ZIP reported the same missing placeholder by row ID and passed after the placeholder was restored. The handoff guide maps that issue to a draft status and a specific fix, with in-game review pending until a build is inspected.
- Import and a trial run in the target apps are tracked under P0.3.
