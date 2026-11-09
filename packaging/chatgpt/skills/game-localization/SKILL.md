---
name: game-localization
description: Translate, edit, and review video game UI, tutorials, dialogue, subtitles, store text, and project documentation for Steam, PlayStation, Xbox, and mobile games. Use for game string batches, glossary creation and enforcement, locale selection, localization QA, and localization of game or skill READMEs.
license: MIT
---

# Game Localization

Read [the localization rules](references/game-localization-rules-v0.1.md) before processing project text. They contain the complete editing and acceptance rules and the 30-entry language preset. Apply them to the current project's materials. Ask the team for missing platform-specific requirements and record any unverified requirements.

Use the [30-edition starter glossary](references/glossary/README.md) for candidates. Read the relevant target edition and match the term ID to its English context. Project-approved entries govern the translation. Never promote a reference entry or a newly suggested term to approved without the project's confirmation.

When the user wants to try the skill on sample data, offer the bundled [first-run example](examples/first-run/README.md).

## Start a project

1. Treat the glossary choice as a prerequisite for the first translation batch. Use the current glossary if supplied. If the user has already asked to build one, start a draft from the [project glossary template](references/project-glossary-template.md). Otherwise, when the glossary is missing, ask the user to supply it or authorize building a draft. End that response after the setup questions and wait for their choice before proposing translations or term candidates. Follow the [project glossary workflow](references/project-glossary.md) when creating, updating, or resuming a glossary.
2. Establish the source language, target locales, material type, and platform when relevant. Use an explicit selection immediately. Otherwise offer the full preset, a subset, or a custom list with additions. Clarify ambiguous regional or script choices when the brief does not resolve them. If source and target locale coincide, supply the source for that locale and separate requested source edits.
3. Request only missing details that affect the result. Use row IDs when available. Continue on clear rows while a meaning-changing ambiguity or conflict waits for an answer. Keep uncertain rows out of the ready-to-import output unless the user explicitly requests a labeled draft of them.

## Translate a batch

- For Steam store copy, use the [Steam store workflow](references/steam-store.md). Return the localized fields separately, check length and claims against the brief, and track Steamworks import and preview separately.
- When a source CSV has changed and translations already exist, follow the [CSV update workflow](references/csv-updates.md). Match stable IDs across revisions, preserve eligible accepted and editor wording, and keep changed rows for review. Save a scene checkpoint for large dialogue batches.
- For a requested `.xlsx` deliverable, follow the [Excel workflow](references/xlsx-qa.md). Confirm the worksheet, header row, stable ID column, source column, and existing target column. Use a new workbook copy and verify it before handoff.
- Establish what each string does in the game. Preserve meaning, mechanics, quantities, conditions, speaker intent, and the relevant voice. Prefer established game UI phrasing when the project glossary allows it. Apply project-specific style settings only to the content they govern.
- Apply approved terms in every applicable occurrence. Match the intended concept, allow only permitted inflection or variants, and preserve exact spellings where required. For each new project term, record the source, locale, proposed equivalent, context, and draft status. Apply a temporary form consistently and mark the affected output as draft while material terms await approval.
- Keep source IDs, keys, protected placeholders, tags, escapes, and significant structure intact. Preserve argument identity, multiplicity, and scope. Reorder only when the format permits it. Use a supported plural mechanism or ask the developer for the missing variant. Never silently resolve an approved-term conflict, a meaning-changing ambiguity, or a hard limit by discarding information.
- Surface proposed source edits separately. Modify source resources only as agreed. Use a clean target artifact and put questions, terminology changes, caveats, and checks outside it.

## Check and hand off

1. Compare source and translation for coverage, meaning, approved terminology, and technical integrity. Check stated limits in the supplied unit. Use format-aware checks when available. For CSV batches with stable IDs, use the [CSV checker](references/csv-qa.md) when the runtime can run it. Review what actual placeholder values render as when examples are available.
2. Review the text in its intended scene or screen. For in-game UI, use the [in-build QA guide](references/in-build-qa.md) to give testers prioritized checks with the screen, string ID, reproduction steps, and expected result. Start with long substitutions and clipping. Estimate width when the required inputs are available and keep build review pending until the scenario is inspected.
3. Use the [handoff guide](references/handoff.md) to return the output separately from the report. Name the deliverable, say how it can be used, and give separate statuses for file checks, language review, and review in the game or preview. Report whether all applicable approved term occurrences were checked and whether any conflicts remain.
4. Record approved decisions in the project glossary. When you create or update a portable glossary, return the complete file separately from the translation and identify proposals in the handoff. Ask for the current glossary in a new session when it is unavailable.
