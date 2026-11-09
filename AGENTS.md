# Game Localization repository instructions

## Resume work

Read [ROADMAP.md](ROADMAP.md) and inspect the Git status before editing. Continue from the recorded next task unless the user changes the order. After verifying a task, update its status, record the verification and identify the next task.

## Complete a product update

Write project documentation and repository instructions in English. Write each localized README in its target language.

1. Update the skill instructions or reference documentation for the behavior that changed. Verify the normal skill workflow and run `python -B -m unittest discover -s tests -v`.
2. Keep the English `README.md` and all localized `docs/README.*.md` editions aligned on user-facing behavior, setup and download links. Use the English change as the source for localization and preserve each locale's wording conventions, commands and paths.
3. For an update to the downloadable skill, bump the version in `packaging/chatgpt/.codex-plugin/plugin.json` once per update and summarize the user-facing changes in [CHANGELOG.md](CHANGELOG.md). Run `python scripts/package.py` to regenerate the GitHub catalog bundle and both ZIPs from the same source. Edit the skill under `game-localization/`. The Claude manifest and `packaging/chatgpt/skills/` are generated files. Run `python scripts/package.py --check` before release. Point every README to the current pair. After validating the new pair, remove superseded ZIPs from `packages/` so the repository contains only the current plugin and standalone archives.
4. Verify that every download link resolves, that both ZIPs contain the intended skill instructions, references and scripts, and that the new behavior works from the extracted packages. Record separately any tests that still need to run in the target apps.
5. Review `git diff --check` and prepare a concise commit title and body. Commit, tag, push or publish only when requested.
