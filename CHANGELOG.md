# Changelog

## 0.1.12 · 2026-11-09

- Added a shared GitHub catalog for installing Game Localization in Claude Code and local Codex.
- Added installation, migration, and update instructions. The catalog bundle and both upload ZIPs are built from the same skill source.

## 0.1.11 · 2026-11-09

- Added a Steam store workflow for the short description and About This Game, with field limits and checks for claims about the game.
- Added a draft helper for supported multilingual Steamworks exports. It preserves other fields and languages and tracks live import separately from local checks.

## 0.1.10 · 2026-11-09

- Added CSV revision comparison by ID. Keep eligible accepted and editor wording for unchanged strings, review added and modified rows, and see removed IDs in a separate report.
- Added scene grouping and checkpoints so long dialogue updates can continue in another chat.

## 0.1.9 · 2026-11-09

- Added prioritized in-game QA checklists with a screen, string ID, reproduction steps, and observable pass criteria for each case.
- Added an optional single-line width estimate for plain UI text when the font and layout measurements are available. Build checks keep their own status.

## 0.1.8 · 2026-11-09

- Added an Excel workflow that writes reviewed translations by ID to one existing target column in a new workbook copy.
- The bundled updater reads back the translated cells and checks preservation of the rest of the workbook before handoff. Unsupported inputs can be handed off as a CSV keyed by ID.

## 0.1.7 · 2026-11-09

- Added a portable project glossary template that keeps approved terms and proposals in separate sections with locale and game context.
- Documented how to save the complete glossary, record a decision for one locale, and reuse the file in another chat.

## 0.1.6 · 2026-11-08

- Added a first-run walkthrough with 12 fictional English strings, a German draft, an approved glossary, a copyable prompt, and an example handoff.
- Both downloadable packages include the sample files, and all 30 README editions link to the walkthrough.

## 0.1.5 · 2026-11-08

- Translation handoffs identify the deliverable and show separate statuses for file checks, language review, and review in the game or preview.
- CSV findings include the affected row, what needs fixing, and the next action. The handoff labels output as a draft when it cannot yet be used as requested.

## 0.1.4 · 2026-11-08

### Added

- Automatic CSV checks for files with stable row IDs. The checker reports missing, unexpected or duplicate IDs, empty translations, changes to supported placeholders or tags, and length limit violations.
- A CSV checker guide with command examples and a sample issue report.
- A development roadmap and repository instructions for resuming work and preparing updates.

### Changed

- Both downloadable skill packages include the CSV checker and its guide.
- All 30 README editions document CSV checks and link to the new packages.

## 0.1.3

- Initial ChatGPT plugin and standalone skill packages with localization rules and a starter glossary of 75 terms across 30 languages and locales.
