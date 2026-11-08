# Video Game Localization Rules

Use these rules when translating or reviewing game text. Work from the source, context, and materials supplied by the project team.

## 1. Purpose and scope

- Write text that feels native to the game and its audience. Preserve meaning, function, speaker voice, and the intended effect on the player.
- Check that players can tell what to do, under which conditions, and with what result. Preserve numbers, signs, units, negation, order, direction, certainty, and game mechanics. Adapt syntax and idioms within those bounds.
- Separate general localization practice, target-locale conventions, platform requirements, and project settings. Apply the relevant requirements for in-game or store text from the brief. Ask the team for missing platform requirements or naming conventions and record those checks as pending.

## 2. Project setup

1. On first contact for a project, ask for the current glossary. Use an attached glossary if it covers the target locale. If the team has none, offer to start a draft from the source and maintain it as the work progresses. Use any starter glossary for candidates. Approved terms come from the project's own glossary.
2. Clarify only missing details that affect the translation. Establish the source language, target locales, material type, and relevant platform. Follow section 2.1 for language selection. As needed, request the screen, adjacent lines, scene, speaker, addressee, actual button behavior, variable format, or hard limits. Identify affected strings by ID.
3. If ambiguity could change an action, condition, speaker, or term meaning, flag the affected strings and ask for a decision. Continue with the other strings. For low-risk ambiguity, use a working assumption and record it separately when it affects the translation.

### 2.1. Select target languages

Establish the source language and target languages before translating. Use a clear selection the user has already made. Otherwise offer three options.

1. **Full preset.** Deliver all 30 entries below. When an entry matches the source language and locale, reuse the source text for that entry. Deliver source-language edits separately when requested.
2. **Subset of the preset.** Deliver the selected entries. Apply any exclusions the user lists.
3. **Custom list.** Use the list provided. It can include additional languages or locales, either on their own or alongside the preset.

If the user specifies only Spanish, Portuguese, or Chinese and the brief does not determine the intended variant, ask. Clarify other regional or script choices when they matter. Deliver each variant separately and apply its own glossary. If the game, store page, and documentation use different language sets, track them separately. The requested set defines the work. Record platform support and QA status independently.

| Preset label | Language or variant |
| --- | --- |
| ENGLISH | English |
| FRENCH | French |
| ITALIAN | Italian |
| GERMAN | German |
| SPANISH - SPAIN | Spanish (Spain) |
| BULGARIAN | Bulgarian |
| CZECH | Czech |
| DANISH | Danish |
| DUTCH | Dutch |
| FINNISH | Finnish |
| GREEK | Greek |
| HUNGARIAN | Hungarian |
| INDONESIAN | Indonesian |
| JAPANESE | Japanese |
| KOREAN | Korean |
| MALAY | Malay |
| NORWEGIAN | Norwegian |
| POLISH | Polish |
| PORTUGUESE - BRAZIL | Portuguese (Brazil) |
| PORTUGUESE - PORTUGAL | Portuguese (Portugal) |
| ROMANIAN | Romanian |
| RUSSIAN | Russian |
| SIMPLIFIED CHINESE | Chinese (Simplified script) |
| SPANISH - LATAM | Spanish (Latin America) |
| SWEDISH | Swedish |
| THAI | Thai |
| TRADITIONAL CHINESE | Chinese (Traditional script) |
| TURKISH | Turkish |
| UKRAINIAN | Ukrainian |
| VIETNAMESE | Vietnamese |

## 3. Glossary

- Use the current project glossary for each target locale. In a new session, use the supplied version or request it. Keep proposed and approved entries separate.
- Record the source term, target locale, proposed or approved equivalent, meaning or example, scope, and status. Add permitted inflections, exact spelling, do-not-translate rules, or approved short forms when needed. Create separate entries for different senses of the same word.
- Apply the approved equivalent in every applicable occurrence. Use the required grammatical form when the entry allows inflection. Preserve exact spelling for fixed forms and names that must stay in the source language. Restructure the sentence around the term when useful.
- Propose new terms with context and use temporary forms consistently. Mark them as drafts until the project owner approves them. Label the affected output as draft while material terms await approval. After a glossary change, review affected translations that are available.
- If an approved term conflicts with a platform requirement or hard limit, try revising the surrounding text. If the conflict persists, report the ID, requirements, and proposed resolution separately. Get approval before changing an approved term.
- To pass terminology QA, check every applicable occurrence of every approved term against the current glossary and its agreed exceptions. Report incomplete checks and discrepancies in the batch status.

## 4. Work with the source

- Review the source and context before translating. For an obvious typo or grammar error with one clear reading, translate the intended meaning. Offer a source correction separately when useful to the team, in the original language.
- Ask the author about edits that could affect a mechanic, number, condition, plot point, intentional dialect, or voice. Change the source resource only as agreed, regardless of its language.
- Preserve meaningful pauses, repetition, irony, implication, emotion, and ambiguity. For language-dependent jokes or wordplay, look for a line that performs the same function in the scene and has a similar effect.

## 5. Style by material type

| Material | Rule |
| --- | --- |
| Buttons and menus | Use short, familiar wording. Make actions clear and use a consistent pattern for related labels. Where the glossary leaves a choice open, use familiar gaming terminology for the locale. |
| Tutorials and system messages | Put the required action and its condition where the player will see them. A restrained, practical tone suits technical guidance when it fits the game. |
| Dialogue and narrative | Preserve the character's voice, form of address, relationships, pace, and genre. Read lines with their neighbors. |
| Subtitles | Account for time on screen, sense breaks, and speaker changes. Follow requirements for meaningful sound cues in captions for deaf and hard-of-hearing players. Change timecodes only within the agreed scope. |
| Store pages | Match the source's level of expressiveness. Claims about features, availability, awards, or supported languages must come from the source or project data. |
| READMEs and documentation | Preserve structure, example meaning, and reproducibility. Protect commands, filenames, code syntax, and link destinations. Apply the documentation glossary. |

## 6. Length, case, and technical integrity

- With no hard limit, prefer compact text once meaning and readability are secure. When a limit is specified, use its stated unit. If the text cannot fit without losing important information, flag the constraint and propose a resolution. Check character count and on-screen width separately.
- Preserve meaningful case emphasis, including ALL CAPS, when the project requires it and the target script supports it. Use locale conventions for normal case and headings. Follow the project's punctuation pattern for short UI labels, such as buttons without a final period. In prose, preserve punctuation's function using local conventions.
- Apply the agreed project typography. If the style profile disallows em dashes, restructure sentences while preserving the character in protected data. Ask the team to resolve conflicts between project rules and locale conventions.
- Protect keys, IDs, placeholders, control sequences, tags, escaping, and significant line breaks. Preserve exact token spelling and occurrence counts. Reorder tokens only if the format allows it and their binding and scope stay intact. Check that positional arguments still refer to the right values.
- Distinguish code from displayed text. Preserve a token such as `%M`. Space a displayed percent sign according to the locale or project. Preserve `ESC`, `ADS`, and `FPS` when protected by the schema or glossary. Check button and gesture labels against the device and approved terminology. Ask for missing specifications when needed.
- Test substitutions with representative numbers, grammatical genders and cases, and long values. Use a supported plural mechanism or complete message instead of concatenated fragments only when the format allows it. Raise missing format support with the developer.

## 7. Editorial pass

Read the translation as it will appear in the scene or UI. Revise wording that obscures an action, sounds unnatural, or changes a speaker's voice. Keep expressive devices that do the same job as in the source.

| Check | What to do |
| --- | --- |
| Empty emphasis and marketing clichés | Remove added praise or inflated epithets. Restore the specific action or feature from the source. |
| Formulaic rhetoric | Remove invented contrasts, three-part lists, repetition, or framing that serves no function in the original. |
| Mechanical syntax and calques | Recast sentences in natural target-language phrasing. Untangle modifiers that make the actor or action unclear. Use a consistent pattern for comparable UI elements. |
| Gratuitous synonyms | Repeat the approved term for the same entity. Remove repetition that contributes neither to meaning nor to voice. |
| Plausible invention | Check added details, names, and cause-and-effect statements against the source and context. Preserve the original degree of certainty. |
| Bureaucratic nominalizations | Name an action with a verb where the player needs to act. For example, use `Quit` on a confirmation button and `Exit Game` for the dialog title if appropriate. |
| Added formatting | Keep meaningful structure and markup. Add emphasis, lists, or emoji only if the format or agreed style calls for them. |
| Chat commentary in the resource | Put only the requested content in the deliverable. Keep questions, caveats, alternatives, and comments in the handoff. |

Illustrative EN → ru-RU examples use fictional context.

| Source and context | Translation or next step |
| --- | --- |
| “Hold {interact} to open the airlock”, with «шлюз» approved | `Удерживайте {interact}, чтобы открыть шлюз`. The token stays intact and the action is clear. |
| “The alarm may trigger if you enter before 06:00” | `Если войдёте до 06:00, может сработать сигнализация`. The time, condition, and possibility are preserved. |
| “Clear”, no ID or purpose given | Ask for context. A button might be «Очистить», a status «Чисто», and a command «Освободить». |

## 8. Workflow and handoff

1. Obtain the glossary or agree to work from a draft. Gather context and limits. Identify protected elements.
2. Analyze the source and any ambiguities. Check terms and choose a style suited to the material.
3. Translate for accuracy and readability, then fit the agreed limits.
4. Read the target independently, then compare it with the source for meaning, numbers, coverage, approved terms, tokens, structure, limits, and suitability for the material.
5. Deliver the agreed format. Preserve the schema, keys, and metadata in structured resources. Keep questions by ID, source corrections, glossary proposals, and the status of each QA stage in a separate handoff. Identify strings that require a decision or an in-build check.

## 9. QA and acceptance

| Check | Completion criteria |
| --- | --- |
| Technical QA | All strings are present and keys, structure, protected tokens, and constraints are intact. Use a format-aware check when available. Test substitutions with representative values when available. |
| Target-language review | The text reads naturally in the scene or UI. After reading the target, compare it with the source and check all applicable approved terminology. For independent review, give a target-language editor the translation and game context without identifying how the translation was produced. |
| In-build QA | Inspect the lines on screen or in the scene. For UI, check clipping, wrapping, scaling, fonts, and text direction where relevant. For subtitles, check display timing and speaker changes. |

Use the [handoff guide](handoff.md) to report each check and the next action. A batch passes once required checks are complete and discrepancies are resolved or exceptions are agreed.
