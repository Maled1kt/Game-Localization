# Game Localization roadmap

**Current status.** The `0.1.12` catalog is on `main`, and the project owner confirmed that Claude Code accepted it. The `0.1.13` update simplifies the catalog and moves the bundle to `packaging/plugin/`. Local Codex upgraded an existing installation in an isolated Git test. [Catalog guide](docs/plugin-catalog.md) · [Changelog](CHANGELOG.md)

**Next task.** P3.1. Confirm the baseline installation in both clients, publish `0.1.13` on `main`, and verify that both clients load the update automatically.

To resume work in a new session, read this file and [AGENTS.md](AGENTS.md), inspect `git status`, and continue the next task. Update the status and identify the next task after verifying the work.

## P0 · Verifiable CSV translation

- [x] **P0.1. Check CSV before handoff.** Match rows by ID and flag missing, unexpected or duplicate IDs, empty translations, changes to common placeholders and tags, and length limit violations. Return a JSON report with issues by row. [Checker](game-localization/scripts/check_csv.py) · [Tests](tests/test_check_csv.py)
- [x] **P0.2. Separate the translation and handoff.** Turn CSV findings into plain-language items with the row ID, the problem, and the next action. Report file, language, and in-build checks separately. Label output as draft while an issue blocks import. [Handoff guide](game-localization/references/handoff.md)
- [x] **P0.3. Add a first-run example.** Ship the walkthrough and verify it in both target apps.
  - [x] Ship the fictional 12-row CSV, draft, glossary, prompt, and expected handoff in both ZIPs. Link to the [walkthrough](game-localization/examples/first-run/README.md) from every README.
  - [x] The project owner confirmed the manual import and walkthrough checks in ChatGPT and Claude.

## P1 · Working with a real project

- [x] **P1.1. Make the project glossary portable.** Provide a template with locale, context, and term status. Save approved decisions in a file for the next chat and list proposed terms separately. [Project glossary template](game-localization/references/project-glossary-template.md)
- [x] **P1.2. Verify Excel workbooks.** For supported `.xlsx` files, write translations by ID to the requested column in a new copy and verify preservation of the rest of the workbook. Record the scope of a possible JSON workflow. [Excel workflow](game-localization/references/xlsx-qa.md) · [Tests](tests/test_update_xlsx.py)
- [x] **P1.3. Give testers specific in-build checks.** Identify the screen, string ID, and conditions for each check. Start with long substitutions and clipped text. Add width estimates when font and layout parameters are available. [Checklist and examples](game-localization/references/in-build-qa.md)

## P2 · Translation updates and Steam

- [x] **P2.1. Process changes by ID.** Identify new, modified, and removed rows, reuse accepted translations, and preserve editor changes. Add scene-level checkpoints for large dialogue batches. [CSV update workflow](game-localization/references/csv-updates.md) · [Tests](tests/test_prepare_csv_update.py)
- [x] **P2.2. Add a Steam store page workflow.** Return translations by field with length and fact checks. Verify the import format through a trial import using a real Steamworks export.
  - [x] Ship the field workflow and validate a draft locally using a real multilingual export. [Workflow and example](game-localization/references/steam-store.md) · [Tests](tests/test_prepare_steam_store.py)
  - [x] Confirm that Steamworks accepts the trial file and that the target locale preview shows the expected descriptions.

## P3 · GitHub distribution and automatic updates

- [ ] **P3.1. Publish Game Localization through a shared GitHub plugin catalog.** Serve the plugin files for Claude Code and local Codex from `main` and bump the plugin version with each release. Document first-time installation, switching from ZIP, and how each client checks for updates. Keep the current ZIP pair available for manual installation. Done when a plugin installed from the catalog in each client automatically loads a newer release published to `main`. [Claude Code marketplace guide](https://code.claude.com/docs/en/plugins/host-marketplace) · [Codex marketplace guide](https://developers.openai.com/plugins/build/plugins#how-local-marketplaces-work)
  - [x] Build the shared catalog bundle and both ZIPs from one skill source. Document first-time installation, switching from ZIP, and refresh in each client.
  - [x] Verify Codex installation and refresh in an isolated local Git repository.
  - [x] Publish the baseline catalog to GitHub. The project owner confirmed that Claude Code accepted it.
  - [ ] Confirm the baseline plugin installation from GitHub in both clients.
  - [ ] Verify a later GitHub release with Claude Code auto-update enabled and an unattended Codex refresh.

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
- Download and walkthrough links resolved in all 30 README editions. The project owner confirmed that package import and the walkthrough passed in ChatGPT and Claude.

## Version 0.1.7 verification

- All six CSV tests passed. Both ZIPs rebuilt byte for byte and contained the glossary workflow and template. The download and template links resolved in all 30 README editions.
- The local glossary walkthrough saved and reopened a complete glossary from each extracted template. The approved German entry and unrelated approved entry were retained, and the Brazilian Portuguese proposal stayed pending.
- Manual app verification is pending. In ChatGPT and Claude, approve one locale's term, save the returned glossary, and attach it in a new chat to confirm that the approved wording is reused and the other proposal stays pending.

## Version 0.1.8 verification

- All ten regression tests passed. The Excel tests cover shared and inline text, missing target cells, ID matching, styles, formula protection, merged ranges, duplicate and unknown IDs, and existing output paths.
- Both ZIPs rebuilt byte for byte. The updater from each extracted ZIP wrote the expected cells. A separate workbook reader confirmed literal text, cell styles, column width, source cells, the neighboring formula, and the second sheet. All 60 archive links and 30 Excel guide links resolved locally.
- Manual app verification is pending. In ChatGPT and Claude, attach a two-sheet workbook and ask for a new copy with one translated column. Open that copy in Excel, confirm that it opens without repair, and verify that the intended values, styles, formula, and second sheet are present.
- A first JSON workflow is feasible for UTF-8 files whose top-level object maps stable keys to strings. Use a duplicate-aware parse, compare key coverage and protected tokens, and verify a new output file. Treat nested objects, arrays, mixed value types, and engine-specific formats as separate work. JSON editing is deferred and does not change the task order. [JSON object rules](https://www.rfc-editor.org/rfc/rfc8259#section-4)

## Version 0.1.9 verification

- All ten regression tests passed. Both ZIPs rebuilt byte for byte. All 60 archive links and 30 in-build guide links resolved locally.
- The extracted German examples in both packages identify `TUT_014` with a long input binding and `MENU_005` with a narrow viewport. Both build checks remain pending in the fictional walkthrough.
- The extracted estimator measured the short button label at 52 px and the substituted airlock prompt at 524 px against a 220 px budget in Segoe UI at 18 px. It rejected multiline input and right-to-left input without Raqm. The Raqm shaping path remains untested in the local runtime.
- Manual app verification is pending. In ChatGPT and Claude, run the first-run prompt and check that the handoff includes the two cases, identifies their screens and IDs, gives steps and pass criteria, and keeps both pending while the build is unavailable.

## Version 0.1.10 verification

- All fourteen regression tests passed. The CSV update tests cover preserved editor wording, changed text and context, scene moves, deleted IDs, blank editor values, placeholder conflicts, and protection against overwriting the working file.
- Both ZIPs rebuilt byte for byte. From each extracted ZIP, the German example produced a new draft with two carried translations and two review rows. A local walkthrough reopened a scene checkpoint, finished the next scene without losing earlier work, and passed the CSV checker on all four current IDs.
- All 60 archive links and 30 CSV update guide links resolved locally.
- Manual app verification is pending. In ChatGPT and Claude, use the guide's example, save a checkpoint after Docking, and resume Control room in a new chat. Confirm that the editor's wording and the reviewed Docking line carry over and that the deleted ID stays out of the working CSV.

## Version 0.1.11 verification

- All eighteen regression tests passed. Both ZIPs rebuilt byte for byte, and all 60 archive links and 30 Steam guide links resolved locally.
- The helper from each extracted ZIP passed the fictional example and read the project-provided export of 30 languages with 11 fields per language. The unchanged round trip retained all 330 field values. A separate local trial changed only the two selected German description fields. The actual store export and its trial copy are outside the repository.
- The project owner confirmed that the trial import and German preview worked in Steamworks on 2026-11-09.
- Manual ChatGPT and Claude verification remains pending. Use the guide's fictional example to check the field handoff and fact review.

## Version 0.1.12 verification

- All eighteen regression tests passed. Both ZIPs rebuilt byte for byte, the bundled first-run checker found the expected three draft issues, and all 60 download links and 30 catalog guide links resolved locally.
- The package check validated the two manifests and skill files against the release source. An isolated test confirmed it rejects a stale generated skill and that rebuilding restores it.
- Codex CLI installed `game-localization@maled1kt` version `0.1.12` from the shared catalog. In an isolated Git fixture, `marketplace upgrade` advanced the installed plugin to test version `0.1.13` and loaded the changed skill file.
- The `0.1.12` baseline reached `main`, and the project owner confirmed that Claude Code accepted the catalog. The two-client update trial is tracked under P3.1.

## Version 0.1.13 verification

- All eighteen regression tests passed. Both ZIPs rebuilt byte for byte and the bundled first-run checker found the expected three draft issues. All 60 download links and 30 catalog guide links resolved locally.
- Codex CLI upgraded the committed `0.1.12` plugin to `0.1.13` in an isolated Git repository after the bundle moved. The existing plugin ID stayed enabled and the installation and authentication defaults remained `AVAILABLE` and `ON_INSTALL`.
- GitHub publication and the unattended refresh trial in Claude Code and Codex are pending.
