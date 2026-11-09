# Carry a project glossary between chats

Use the project's current glossary in its existing format. When the user asks to start a glossary or export a portable copy, use the [Markdown template](project-glossary-template.md). Name the new file `project-glossary.md` unless the user specifies another name. Record the project and source locale. Keep the glossary separate from the translation and the handoff.

## Record terms and decisions

- The **Approved terms** and **Proposed terms** sections record each entry's status. Use the approved section as the terminology authority for the matching project, target locale, and sense. Use the [starter glossary](glossary/README.md) and new suggestions as proposals until the project approves them.
- Identify entries by term ID and target locale. Reuse an existing project ID when available. Give different senses different IDs, even when their source spelling matches. Record the game context, applicable scope, and any fixed forms, allowed inflections, or approved short forms that affect usage.
- Keep proposals separate from approved decisions in the file and the handoff. Give each proposal's ID, locale, context, and suggested wording. If a proposal would change an approved form, keep applying the current form until the project approves the replacement or resolves the conflict.
- Apply an explicit approval only to the indicated entry and locale. Record the exact approved wording and constraints. Move that proposal to the approved section or update the matching approved entry, and keep unrelated entries and pending proposals. If the approval could refer to more than one entry or locale, ask which one it covers. Review affected translations that are available.

## Save and resume

- After creating or updating a portable glossary, return the complete current file. When recording a decision in an existing glossary, return the updated glossary in its existing format. Update the supplied file in place when the user asks for that. If file tools are unavailable, return the complete glossary content separately so the user can save it.
- Ask the user to save the latest version and attach it in the next chat. When they provide it, use it for the identified project and target locales. If competing versions disagree, ask which version governs the affected entries and proceed with entries that have a clear decision.

## Example

In the first chat, the team proposes `Luftschleuse` for `TERM-001` in `de-DE` and `eclusa de ar` for the same ID in `pt-BR`. The owner replies, “Approve `TERM-001` in `de-DE` as `Luftschleuse`.” The German entry moves to **Approved terms** and the Brazilian Portuguese entry stays in **Proposed terms**. Return the complete glossary with both rows.

In the next chat, the owner attaches that file and asks for a German docking tutorial. Use `Luftschleuse` for the same airlock. Report the Brazilian Portuguese proposal only when it is relevant to the requested work.
