# Game Localization

![Game Localization by Maled1kt](assets/game-localization-banner.png)

Game Localization is an Agent Skill for translating, editing, and reviewing video game text in ChatGPT, Codex, and Claude. It covers menus, tutorials, dialogue, subtitles, store copy, and project documentation for Steam, PlayStation, Xbox, and mobile games.

Get a translation and a separate QA report.

**[Install](#install)** · **[Try the 12-row example](game-localization/examples/first-run/README.md)** · [Use the skill](#use-the-skill) · [Support the author](#support-the-author)

## Languages

The localized editions of this README were translated with Game Localization. Choose a language below to see how it reads.

<details>
<summary>Choose a language (30 editions)</summary>

**English** (default) · [Français](docs/README.fr.md) · [Italiano](docs/README.it.md) · [Deutsch](docs/README.de.md) · [Español (España)](docs/README.es-ES.md) · [Български](docs/README.bg.md)

[Čeština](docs/README.cs.md) · [Dansk](docs/README.da.md) · [Nederlands](docs/README.nl.md) · [Suomi](docs/README.fi.md) · [Ελληνικά](docs/README.el.md) · [Magyar](docs/README.hu.md)

[Bahasa Indonesia](docs/README.id.md) · [日本語](docs/README.ja.md) · [한국어](docs/README.ko.md) · [Bahasa Melayu](docs/README.ms.md) · [Norsk bokmål](docs/README.nb.md) · [Polski](docs/README.pl.md)

[Português (Brasil)](docs/README.pt-BR.md) · [Português (Portugal)](docs/README.pt-PT.md) · [Română](docs/README.ro.md) · [Русский](docs/README.ru-RU.md) · [简体中文](docs/README.zh-Hans.md) · [Español (Latinoamérica)](docs/README.es-419.md)

[Svenska](docs/README.sv.md) · [ไทย](docs/README.th.md) · [繁體中文](docs/README.zh-Hant.md) · [Türkçe](docs/README.tr.md) · [Українська](docs/README.uk.md) · [Tiếng Việt](docs/README.vi.md)

</details>

## Install

| Where you work | Package |
| --- | --- |
| ChatGPT or Codex with plugin upload access | [ChatGPT plugin ZIP](packages/game-localization-chatgpt-v0.1.13.zip) |
| Claude or eligible ChatGPT workspaces with standalone skill upload | [Standalone skill ZIP](packages/game-localization-skill-v0.1.13.zip) |
| Local Codex or Claude Code with plugin support | [Install from the GitHub catalog](docs/plugin-catalog.md) |

On GitHub, open the package link and choose **Download raw file**. Keep the ZIP intact for upload.

[Installation details](#setup-details) · [Install from the source folder](#one-command-install-for-local-agents)

## Use the skill

### How it works

```mermaid
flowchart TD
    A["Source files and brief"] --> B["Approved glossary or draft"]
    B --> C["Translation and checks"]
    C --> D["Translation or labeled draft"]
    C --> E["Separate QA report"]
```

1. Attach the source text or file and the current project glossary for the target locales. If you have no glossary, explicitly ask the skill to start a draft.
2. Specify the source and target locales, platform, material type, and output format. Include character limits, screenshots, speaker notes, or variable examples where they matter.
3. For a spreadsheet, name the source and target columns and ask for a new copy. For in-game strings, provide stable IDs or keys. For store text, include the target field and any hard length limit.
4. Read the separate handoff to see whether the output is ready to use or still a draft. It reports file checks, language review, and review in the game or store preview separately, with a next action for each open issue. Approve terms in your project glossary before reusing them.

### Choose a workflow

| Format | Provide | Get |
| --- | --- | --- |
| [CSV](game-localization/references/csv-qa.md) | CSV with stable row IDs (previous files for updates) | Checked translation or change report |
| [Excel](game-localization/references/xlsx-qa.md) | Workbook, sheet, and ID, source, and target columns | Verified workbook copy |
| [Steam](game-localization/references/steam-store.md) | Store copy or Steamworks export | Localized fields or JSON draft |

<details>
<summary>Prompt examples and file checks</summary>

For in-game UI, the handoff includes a prioritized checklist with screens, string IDs, reproduction steps, and pass criteria. It starts with long substitutions and text that could clip. If the font and usable width are known, the skill can estimate how much room the text needs. [In-build QA guide](game-localization/references/in-build-qa.md)

Use the [project glossary template](game-localization/references/project-glossary-template.md) to keep approved terms and proposals separate. Save the updated file and attach it to your next chat.

**Spreadsheet prompt**

~~~text
Use Game Localization to translate ENGLISH into German (de-DE) on the
Strings worksheet. Match rows by ID and write to the existing GERMAN
column in a new .xlsx copy. Use the glossary and DESCRIPTION column
for context. Preserve source columns, placeholders, and tags.
List terminology questions and checks separately, with row IDs.
~~~

For supported `.xlsx` files, specify the worksheet, header row, stable ID column, source column, and existing target column. With Python 3.9 or later, the skill writes by ID to a new copy and checks that the rest of the workbook was preserved. If the workbook cannot be verified, the skill can offer a CSV keyed by ID. [Excel instructions](game-localization/references/xlsx-qa.md)

**Store page prompt**

~~~text
Use Game Localization to localize this Steam short description from
English into Brazilian Portuguese (pt-BR). Start a draft glossary if
needed. Keep the game title unchanged and stay within the supplied
character limit. Return the store copy and a separate handoff.
~~~

For Steam pages, the skill returns the short description and About This Game separately, checks the supplied limits and product claims, and can prepare a draft from a supported Steamworks JSON export. The handoff tracks import and preview separately. [Steam store workflow](game-localization/references/steam-store.md)

### Check CSV translations

For a CSV with stable row IDs, specify the ID, source, and translation column headers. With Python 3.9 or later, the skill compares the source and translated files and flags missing or duplicate IDs, empty translations, changes to supported placeholders or tags, and length limit violations. [CSV checker instructions](game-localization/references/csv-qa.md)

To update a translation, attach the previous and current source CSVs, accepted translations, and any later editor changes. The skill matches IDs, keeps eligible wording for unchanged rows, and flags added, changed, and removed rows. For long dialogue batches, save a checkpoint after each scene so you can resume with the same working file. [CSV update guide](game-localization/references/csv-updates.md)

</details>

## What it does

- Applies the project's approved terminology and records new terms as draft candidates.
- Preserves localization keys, placeholders such as `{player_name}` and `%s`, tags, significant line breaks, and other protected tokens.
- Checks stated length limits and keeps translations separate from questions, source corrections, and QA notes.
- Offers a [30-entry language and locale preset](game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages) and accepts custom locale lists.
- Includes a [75-term starter glossary in all 30 languages and locales](game-localization/references/glossary/README.md), with shared English definitions and draft translations.

The skill contains instructions and reference files. It requires no project API key, connector, or background service. File editing depends on the tools available in the selected chat. For release QA, check the translated UI in the game build and store copy in the platform preview.

## Update or remove

| Installation | Update | Remove |
| --- | --- | --- |
| [Install from the GitHub catalog](docs/plugin-catalog.md) | [Claude Code](docs/plugin-catalog.md#claude-code) · [Codex](docs/plugin-catalog.md#local-codex) | [Remove](docs/plugin-catalog.md#remove-the-catalog-installation) |
| ChatGPT or Codex plugin | Use **Upload new version** on the plugin details page when you manage the upload. For directory or workspace installs, updates come from that source. | Open **Plugins → Installed → Game Localization** and choose **Uninstall plugin** where available. Ask the administrator about a managed install. |
| ChatGPT standalone skill | Use the available skill management controls to replace your personal upload with the latest standalone ZIP. | Open **Plugins → Skills**, find the skill under **Installed** or **Created by me**, and use its removal control when available. Workspace admins manage workspace-owned skills. |
| Claude custom skill | Upload the new standalone ZIP from the skill management page. If it creates a second entry, disable the earlier version. | Open the skill in **Customize → Skills** or **Plugins**, switch it off, then use **⋯ → Delete** for a skill you uploaded and confirm. |
| Local skill installed with the Skills CLI | Run `npx skills update game-localization` for a tracked branch, or install from the new tag. | Run `npx skills remove game-localization` from the same project. Add `-g` if you installed it globally. |
| Local folder or Codex Skill Installer | Replace the installed `game-localization/` folder with the latest version. | Remove the installed `game-localization/` folder. Codex can load it from `.agents/skills/`, `~/.agents/skills/`, or the installer location `~/.codex/skills/`. Claude Code uses `.claude/skills/` or `~/.claude/skills/`. Start a new session if needed. |

[OpenAI plugin management](https://learn.chatgpt.com/docs/plugins) · [Claude custom skill management](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

<a name="setup-details"></a>

## Installation details

### ChatGPT and Codex

1. In ChatGPT on the web, open the plugin upload option for your account. Workspace owners and administrators with upload access can use **Admin console → Plugins → Add → Upload plugin**.
2. Select the **ChatGPT plugin ZIP**. Wait for validation, then open **Game Localization** in **Plugins** and select **Install plugin** if offered. A personal upload may appear under **Personal → Created by me**.
3. Start a fresh chat in ChatGPT or Codex. Type `@` and select **Game Localization** from the suggestions.

If your workspace offers standalone skill uploads, go to **Plugins → Skills → Create → Upload from your computer** and use the **standalone skill ZIP**. Wait for the scan and follow any prompts. The available upload and installation options depend on your account and workspace. [OpenAI plugin guide](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [OpenAI skills guide](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. Enable **Code execution and file creation** in Claude settings if required by your account or workspace.
2. In Claude on the web or in Claude Desktop, open **Customize → Skills**. In the newer layout, open **Plugins** from the sidebar and look for the skill controls under **Your plugins**.
3. Select **+ → Create skill → Upload a skill** and choose the **standalone skill ZIP**. Turn on `game-localization` after it appears.
4. Start a fresh chat and ask Claude to use **Game Localization**. If the composer lists the skill under **+** or **/**, select it there.

A managed workspace may require an administrator to enable skills or upload them. [Claude skills guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Claude sidebar rollout](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### One-command install for local agents

<details>
<summary>Show manual installation commands</summary>

In a **local Codex chat**, select the built-in `$skill-installer` and send this request. Approve network access if prompted, then start a fresh session. [Codex skills guide](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

For **local Codex and Claude Code**, the third-party Skills CLI can install the same source folder for both agents in a single terminal command. With Node.js 22.20 or later, run this from the project where you want to use the skill. Select only the agents you need by keeping the corresponding `-a` flags. Add `-g` for a user-wide install. [Skills CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

In the local Claude Code terminal chat, use its shell input to run the Claude-only install directly. Review the repository URL before running it. [Claude Code shell input](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

Open a new session and invoke `$game-localization` in Codex or `/game-localization` in Claude Code. For a manual Claude Code setup, copy the full `game-localization/` folder into `.claude/skills/` in the project or into `~/.claude/skills/` for your user. [Claude Code skills guide](https://code.claude.com/docs/en/skills)

In hosted ChatGPT and Claude, use the account's upload or install controls. A chat mention invokes the installed skill. For a shareable install link, publish through the platform's supported directory or share the skill or plugin within an eligible workspace. [ChatGPT plugin sharing](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Claude skill sharing](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

</details>

## Source and packaging

- [`game-localization/SKILL.md`](game-localization/SKILL.md) defines when the skill runs and how it handles a batch.
- [`game-localization/references/`](game-localization/references/) contains the rules and the locale editions of the starter glossary.
- [`packaging/plugin/`](packaging/plugin/) contains the Codex manifest, icon, and generated catalog bundle for both clients.
- [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json) is the shared catalog.
- [`packages/`](packages/) contains the upload-ready archives.

To rebuild the catalog bundle and both ZIPs from the same source, run `python scripts/package.py` from the repository root with Python 3.9 or later. The version comes from the Codex plugin manifest. Run `python scripts/package.py --check` to verify the generated files. Before distributing a new build, upload each ZIP to its intended product and try a small batch with a glossary and a protected placeholder.

### Our model settings

| Where we work | Model | Reasoning setting |
| --- | --- | --- |
| ChatGPT Work or Codex | GPT-6.1 Sol | High or higher, where available |
| Claude | Claude Opus 5.5 | High or higher, where available |

We use **High+** as shorthand for High or a higher setting exposed by the client. Select the model and effort in your client. The skill works independently of this preference. [OpenAI model settings](https://learn.chatgpt.com/docs/models) · [Claude effort levels](https://platform.claude.com/docs/en/build-with-claude/effort)

[Update or remove](#update-or-remove) · [Development roadmap](ROADMAP.md) · [Changelog](CHANGELOG.md)

## License

Game Localization is available under the [MIT License](LICENSE). Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## Support the author

If Game Localization helps your team, you can [support Maled1kt through DonationAlerts](https://www.donationalerts.com/r/maled1kt). Donations are entirely voluntary.
