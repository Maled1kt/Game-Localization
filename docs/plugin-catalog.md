# Install and update from GitHub

The `maled1kt` catalog provides the Game Localization plugin for Claude Code and local Codex. It tracks the `main` branch. The plugin name in either client is `game-localization@maled1kt`. Use the catalog commands after the catalog files are available on GitHub. The [download ZIPs](../README.md#install) are also available for manual installation.

## Claude Code

1. In a Claude Code session, add the catalog and install the plugin.

   ```text
   /plugin marketplace add Maled1kt/Game-Localization#main
   /plugin install game-localization@maled1kt
   ```

2. In `/plugin`, open **Marketplaces**, select **maled1kt**, and choose **Enable auto-update**. Claude Code checks this catalog in the background after a session starts when that setting is enabled.
3. Start a new session and ask Claude Code to use Game Localization. When an update is downloaded, follow the reload or restart prompt to load the new version.

For an immediate check, run `/plugin marketplace update maled1kt` or `claude plugin update game-localization@maled1kt`. [Claude Code marketplace updates](https://code.claude.com/docs/en/plugins/host-marketplace#keep-users-up-to-date)

## Local Codex

1. In a terminal with the Codex CLI, register the GitHub catalog and install the plugin.

   ```sh
   codex plugin marketplace add Maled1kt/Game-Localization --ref main
   codex plugin add game-localization@maled1kt
   ```

   You can also select **Game Localization** under **maled1kt** in the local Plugins directory after registering the catalog.
2. Open a new Codex chat and select the plugin or ask Codex to use Game Localization. Use `codex plugin list --marketplace maled1kt` to see the installed version.
3. To refresh from GitHub, run `codex plugin marketplace upgrade maled1kt` and open a new session. The official local CLI documents this explicit refresh command. [OpenAI Codex CLI reference](https://learn.chatgpt.com/docs/cli/reference#codex-plugin-marketplace)

### Optional scheduled refresh on Windows

After the refresh command succeeds in your terminal, you can have Windows Task Scheduler run it periodically under the same Windows account. Create a task, choose a daily or sign-in trigger, and add a **Start a program** action. Use the full path to the Codex CLI executable for **Program/script** and `plugin marketplace upgrade maled1kt` for **Add arguments**. In PowerShell, `(Get-Command codex).Source` shows the command's location. Run the task once to check its result. Open a new Codex session after an update. If a Codex upgrade changes the executable path, update the task's program path. [Windows Task Scheduler](https://learn.microsoft.com/en-us/windows/win32/taskschd/using-the-task-scheduler)

## Switch from a ZIP or standalone copy

Install and verify the catalog plugin first. In the local client where you switched, disable or remove the old Game Localization copy to avoid duplicate skill entries. If the old skill was copied into a local skills folder, use the [manual removal instructions](../README.md#update-or-remove). Keep project glossaries and other project files separately so you can reuse them with the catalog plugin.

To remove the catalog installation, uninstall the plugin first. Then use `/plugin marketplace remove maled1kt` in Claude Code or `codex plugin marketplace remove maled1kt` in Codex if you also want to remove the catalog.

## Maintainer release checks

1. Edit the skill under `game-localization/` and bump the version in `packaging/chatgpt/.codex-plugin/plugin.json`. Run `python scripts/package.py` to update the catalog's Claude manifest, bundled skill files, and both upload ZIPs. Run `python scripts/package.py --check` and commit the generated catalog bundle with the source changes.
2. Once a baseline is on `main`, install it from GitHub in both clients and record the version. Publish a later version and verify that Claude Code with marketplace auto-update enabled loads it. In Codex, verify the refresh command and, if using scheduled refresh, verify that the schedule installs the newer version without manual intervention.
3. Open a new session in each client and verify the new skill is available. Record the tested versions and update method in the [Roadmap](../ROADMAP.md).
