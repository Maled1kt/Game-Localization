# Game Localization roadmap

**Current status.** The English-to-German (`de-DE`) P0.3 walkthrough is complete and included in both `0.1.6` packages. The local walkthrough checks passed. [First-run example](game-localization/examples/first-run/README.md) · [Changelog](CHANGELOG.md)

**Next task.** P0.3 manual verification. The project owner will import both ZIPs and try the walkthrough in their intended apps. Record the results before continuing to P1.1.

To resume work in a new session, read this file and [AGENTS.md](AGENTS.md), inspect `git status`, and continue the next task. Update the status and identify the next task after verifying the work.

## P0 · Verifiable CSV translation

- [x] **P0.1. Check CSV before handoff.** Match rows by ID and flag missing, unexpected or duplicate IDs, empty translations, changes to common placeholders and tags, and length limit violations. Return a JSON report with issues by row. [Checker](game-localization/scripts/check_csv.py) · [Tests](tests/test_check_csv.py)
- [x] **P0.2. Separate the translation and handoff.** Turn CSV findings into plain-language items with the row ID, the problem, and the next action. Report file, language, and in-build checks separately. Label output as draft while an issue blocks import. [Handoff guide](game-localization/references/handoff.md)
- [ ] **P0.3. Add a first-run example.** Finish the manual app check to close this item.
  - [x] Ship the fictional 12-row CSV, draft, glossary, prompt, and expected handoff in both ZIPs. Link to the [walkthrough](game-localization/examples/first-run/README.md) from every README.
  - [ ] Manually import the plugin ZIP in an eligible ChatGPT workspace and the standalone ZIP in Claude. Run the walkthrough in both apps and confirm that the handoff reports the two fixes, the open question for `MENU_006`, and the pending in-game review.

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

## Version 0.1.6 verification

- All six CSV tests passed, including the first-run draft, the reviewed copy, and the resolved copy.
- Both ZIPs rebuilt byte for byte. The documented command from each extracted German walkthrough found three issues in the original draft, one issue after the two fixes, and zero issues after `MENU_006` was resolved. Only the current package pair is present in `packages/`.
- Download and walkthrough links resolved in all 30 README editions. The project owner will verify app import and a live run manually.
