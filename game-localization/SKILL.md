---
name: game-localization
description: Translate, edit, and review video game UI, tutorials, dialogue, subtitles, store text, and project documentation for Steam, PlayStation, Xbox, and mobile games. Use for game string batches, glossary creation and enforcement, locale selection, localization QA, and localization of game or skill READMEs.
license: MIT
---

# Game Localization

Read [the localization rules](references/game-localization-rules-v0.1.md) before processing project text. They contain the complete editing and acceptance rules and the 30-entry language preset. Apply them to the current project's materials. Ask the team for missing platform-specific requirements and record any unverified requirements.

Use the [30-edition starter glossary](references/glossary/README.md) for candidates. Read the relevant target edition and match the term ID to its English context. Project-approved entries govern the translation. Never promote a reference entry or a newly suggested term to approved without the project's confirmation.

## Start a project

1. Treat the glossary choice as a prerequisite for the first translation batch. Use the current glossary if supplied. If the user has already asked to build one, start a draft. Otherwise, when the glossary is missing, ask the user to supply it or authorize building a draft. End that response after the setup questions and wait for their choice before proposing translations or term candidates. Keep candidates and approvals separate by locale and project.
2. Establish the source language, target locales, material type, and platform when relevant. Use an explicit selection immediately. Otherwise offer the full preset, a subset, or a custom list with additions. Clarify ambiguous regional or script choices when the brief does not resolve them. If source and target locale coincide, supply the source for that locale and separate requested source edits.
3. Request only missing details that affect the result. Use row IDs when available. Continue on clear rows while a meaning-changing ambiguity or conflict waits for an answer. Keep uncertain rows out of the ready-to-import output unless the user explicitly requests a labeled draft of them.

## Translate a batch

- Establish what each string does in the game. Preserve meaning, mechanics, quantities, conditions, speaker intent, and the relevant voice. Prefer established game UI phrasing when the project glossary allows it. Apply project-specific style settings only to the content they govern.
- Apply approved terms in every applicable occurrence. Match the intended concept, allow only permitted inflection or variants, and preserve exact spellings where required. For each new project term, record the source, locale, proposed equivalent, context, and draft status. Apply a temporary form consistently and mark the affected output as draft while material terms await approval.
- Keep source IDs, keys, protected placeholders, tags, escapes, and significant structure intact. Preserve argument identity, multiplicity, and scope. Reorder only when the format permits it. Use a supported plural mechanism or ask the developer for the missing variant. Never silently resolve an approved-term conflict, a meaning-changing ambiguity, or a hard limit by discarding information.
- Surface proposed source edits separately. Modify source resources only as agreed. Use a clean target artifact and put questions, terminology changes, caveats, and checks outside it.

## Check and hand off

1. Compare source and translation for coverage, meaning, approved terminology, and technical integrity. Check stated limits in the supplied unit. Use format-aware checks if available and review what actual placeholder values render as when examples are available.
2. Reread the text as it appears in the scene or UI. Track technical checks, target-language review, and build review separately. Record a check as complete only when its required evidence is available. A clean string file alone does not verify layout or render behavior.
3. Return output in the requested format and a separate handoff identifying unresolved rows, draft term decisions, and actual review status. Report whether all applicable approved term occurrences were checked and whether any conflicts remain.
4. When the project approves a candidate, carry its new status and exact decision into the next batch. If the user wants a reusable glossary, return the updated entries or update the designated glossary file. Ask for the current glossary in a new session when it is unavailable.
