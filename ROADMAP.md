# Game Localization roadmap

**Current status.** P0.1 is complete. Version `0.1.4` checks CSV before handoff when stable IDs and a Python runtime are available. [CSV technical QA](game-localization/references/csv-qa.md) · [Changelog](CHANGELOG.md)

**Next task.** P0.2. Give users a short handoff with separate statuses for file checks, language review, and in-build review.

To resume work in a new session, read this file and [AGENTS.md](AGENTS.md), inspect `git status`, and continue the next task. Update the status and identify the next task after verifying the work.

## P0 · Verifiable CSV translation

- [x] **P0.1. Check CSV before handoff.** Match rows by ID and flag missing, unexpected or duplicate IDs, empty translations, changes to common placeholders and tags, and length limit violations. Return a JSON report with issues by row. [Checker](game-localization/scripts/check_csv.py) · [Tests](tests/test_check_csv.py)
- [ ] **P0.2. Separate the translation and handoff.** Turn CSV findings into plain-language items with the row ID, the problem, and the next action. Report file, language, and in-build checks separately. Label output as draft while an issue blocks import. Done when a user can tell from the handoff which file they received and what to do next.
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
