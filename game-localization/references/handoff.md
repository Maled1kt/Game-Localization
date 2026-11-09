# Translation handoff

Return the requested translation in its own file or clearly separated content block. Give the handoff in the user's language and keep it outside importable content. State what you returned and what the user can do with it before listing checks. Name files and locales when applicable.

## Say how the output can be used

- **Ready for import** or **Ready for use** applies to the full requested output when checks required for that use have passed and blockers are resolved. If build or preview review is a later step, name it as pending. Import readiness is a file and content decision. Release readiness requires the project's release checks.
- **Draft for review** applies when the output is partial, a blocker remains, or a required check for the requested use is pending. Say what was included and what blocks the requested use. Include meaning-ambiguous rows in a labeled draft only when the user requests them.
- If you could deliver no translation, say what is needed to proceed. For a review-only task, name the artifact reviewed and state its readiness based on the available evidence.

## Report three checks

- **Passed** means the applicable checks at this stage were completed and issues resolved. Cite the evidence.
- **Needs action** means a known issue needs a fix or decision. Give the next action.
- **Pending** means a check still needs to be run or evidence is missing. Say what is needed.
- **Not applicable** means the check falls outside the requested scope. Give a brief reason.

Separate files or locales with different outcomes.

| Check | What to report |
| --- | --- |
| File checks | Say which keys, format, protected tokens, and limits were checked, and whether the check used a tool or was manual. Give coverage when known. For CSV findings, use the [issue guide](csv-qa.md#explain-csv-findings). If a tool could not run, report the manual scope and any pending checks. |
| Language review | Say which meaning, style, and terminology checks were completed. Distinguish agent review from human review. Identify unresolved questions and draft or conflicting terms. Mark required review that lacks context or a reviewer as pending. |
| In-game or preview review | Say what was actually inspected and its scope. For in-game UI, use the [in-build QA checklist](in-build-qa.md) for steps, conditions, and pass criteria. Mark cases pending when the required evidence is unavailable. For a store preview, name the view and fields to inspect. |

For each unresolved issue, give the string ID, the problem in plain language, and one next action. Use the file, field, or record number when there is no ID. Keep the summary short and put long issue lists in a separate report when file tools are available.

For a translation update, summarize changed source IDs and preserved translations, and give the next decision for each blocked ID. For large dialogue updates, return the [scene checkpoint](csv-updates.md#save-progress-by-scene) separately from the working translation.

## Example handoff

> **Ready for import.** `ui.de-DE.csv` contains all 12 requested strings.
>
> - **File checks passed.** The CSV checker matched all 12 IDs and verified supported tokens. The column layout was also checked against the import schema.
> - **Language review passed.** The agent checked meaning and applied the approved glossary to all applicable strings.
> - **In-game review pending.** In `de-DE`, open the pause menu at the highest supported text scale and locate the resume button (`MENU_008`). Pass if the full label is visible inside the button without covering the input icon.
