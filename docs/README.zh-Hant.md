# Game Localization

![Game Localization 橫幅，兩個遊戲對話框交換多種語言的字元](../assets/game-localization-banner.png)

[English](../README.md) · [所有語言](../README.md#languages)

Game Localization 是一項代理技能，可在 ChatGPT、Codex 和 Claude 中翻譯、編輯及校對遊戲文字。適用於 Steam、PlayStation、Xbox 和行動遊戲的選單、教學、對白、字幕、商店文案與專案文件。

[安裝](#安裝) · [使用技能](#使用技能) · [更新或移除](#更新或移除) · [支持作者](#支持作者)

## 功能

- 採用專案核准的術語，並將新術語記錄為候選譯法。
- 保留在地化鍵值、`{player_name}` 和 `%s` 等預留位置、標籤、有意義的換行及其他受保護的元素。
- 檢查指定的長度限制，並將譯文與疑問、原文修正及品管備註分開交付。
- 提供[包含 30 種語言及地區變體的預設清單](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages)，也支援自訂清單。
- 內含[涵蓋全部 30 種語言及地區變體的 75 詞入門詞彙表](../game-localization/references/glossary/README.md)，附有共用的英文定義及候選譯法。

技能包含說明和參考檔案，無需專案 API 金鑰、連接器或背景服務。能否編輯檔案取決於對話中可用的工具。發布前，請在遊戲建置版本中檢查翻譯後的介面，並在平台預覽中檢查商店文案。

## 安裝

| 使用環境 | 安裝套件 |
| --- | --- |
| 有外掛上傳權限的 ChatGPT 或 Codex | [ChatGPT 外掛 ZIP](../packages/game-localization-chatgpt-v0.1.3.zip) |
| Claude 或允許上傳獨立技能的 ChatGPT 工作區 | [獨立技能 ZIP](../packages/game-localization-skill-v0.1.3.zip) |
| 本機 Codex 或 Claude Code | [從原始碼資料夾安裝](#用一個指令安裝到本機代理) |

在 GitHub 開啟套件連結並選擇 **Download raw file**。上傳時保留 ZIP 格式。

### ChatGPT 和 Codex

1. 在 ChatGPT 網頁版中開啟帳號的外掛上傳功能。具上傳權限的工作區擁有者和管理員可使用 **Admin console → Plugins → Add → Upload plugin**。
2. 選擇外掛 ZIP。驗證完成後，在 **Plugins** 中開啟 **Game Localization**，並選擇 **Install plugin**（如有提供）。個人上傳的項目可能出現在 **Personal → Created by me**。
3. 在 ChatGPT 或 Codex 中開啟新對話。輸入 `@`，從建議中選擇 **Game Localization**。

如果工作區支援獨立技能，請透過 **Plugins → Skills → Create → Upload from your computer** 上傳獨立技能 ZIP。等候掃描並按照提示操作。可用選項依帳號和工作區而異。 [OpenAI 外掛指南](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [OpenAI 技能指南](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. 如果帳號或工作區有此要求，請在 Claude 設定中啟用 **Code execution and file creation**。
2. 在 Claude 網頁版或 Claude Desktop 中開啟 **Customize → Skills**。新版介面可從側邊欄開啟 **Plugins**，並在 **Your plugins** 底下找到管理功能。
3. 選擇 **+ → Create skill → Upload a skill** 並上傳獨立技能 ZIP。出現 `game-localization` 後即可啟用。
4. 開啟新對話並請 Claude 使用 **Game Localization**。如果輸入區的 **+** 或 **/** 選單列出此技能，可直接選取。

在受管理的工作區中，可能需要管理員啟用或上傳技能。 [Claude 技能指南](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Claude 側邊欄更新](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### 用一個指令安裝到本機代理

下列指令使用 [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization) 的 `main` 分支。儲存庫和分支發布後即可使用。上方的 ZIP 連結採用相對路徑，也適用於其他分支、標籤及分支複本。

在本機 Codex 對話中選取內建的 `$skill-installer`，送出下方的要求。若出現提示，請允許網路存取，再開啟新工作階段。 [Codex 技能指南](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

第三方 Skills CLI 可用一個終端機指令，將同一個原始碼資料夾安裝到本機 Codex 和 Claude Code。請使用 Node.js 22.20 或更新版本，在目標專案中執行。只保留需要的代理 `-a` 選項。如需安裝給整個使用者帳號，請加上 `-g`。 [Skills CLI 參考](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

在本機 Claude Code 的終端機對話中，可以透過 Shell 輸入直接安裝到 Claude。執行前請確認儲存庫網址。 [Claude Code Shell 輸入](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

開啟新工作階段後，在 Codex 中呼叫 `$game-localization`，或在 Claude Code 中呼叫 `/game-localization`。若要在 Claude Code 手動安裝，請將完整的 `game-localization/` 資料夾複製到專案的 `.claude/skills/` 或使用者的 `~/.claude/skills/`。 [Claude Code 技能指南](https://code.claude.com/docs/en/skills)

使用雲端 ChatGPT 或 Claude 時，請透過帳號的上傳或安裝功能操作。在對話中提及技能即可呼叫已安裝版本。若要分享安裝連結，可發布至平台支援的目錄，或在符合資格的工作區分享技能或外掛。 [分享 ChatGPT 外掛](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [分享 Claude 技能](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## 使用技能

1. 附上原文或來源檔案，以及目標語言的最新專案詞彙表。如果沒有詞彙表，請明確要求先擬一份草稿。
2. 指定來源和目標語言、平台、內容類型和輸出格式。視需要附上字元限制、畫面截圖、說話者說明或變數範例。
3. 試算表請指定來源欄與目標欄，並要求建立副本。遊戲內文字請提供穩定的 ID 或鍵值。商店文案請指定欄位及硬性長度限制。
4. 查看交付說明中的待確認列、暫定術語及已完成的檢查。先在專案詞彙表中核准術語再重複使用，然後在遊戲建置版本或商店預覽中檢查譯文。

**試算表提示詞範例**

~~~text
使用 Game Localization 將附件活頁簿的 ENGLISH 欄翻譯成德語（de-DE），並寫入新 .xlsx 副本的 GERMAN 欄。參考隨附的詞彙表及 DESCRIPTION 欄。保留鍵值、來源欄、預留位置與標籤。另列術語問題和檢查結果，並註明列 ID。
~~~

**商店頁面提示詞範例**

~~~text
使用 Game Localization 將這段 Steam 簡短說明從英文在地化為巴西葡萄牙語（pt-BR）。視需要先擬詞彙表草稿。保留遊戲名稱並遵守指定的字元限制。分別交付商店文案與交付說明。
~~~

### 我們的模型設定

| 使用環境 | 模型 | 推理等級 |
| --- | --- | --- |
| ChatGPT Work 或 Codex | GPT-6.1 Sol | High 或更高（視可用選項而定） |
| Claude | Claude Opus 5.5 | High 或更高（視可用選項而定） |

**High+** 代表用戶端提供的 High 或更高等級。請在用戶端選擇模型和推理等級。技能可在不同等級下使用。 [OpenAI 模型設定](https://learn.chatgpt.com/docs/models) · [Claude 推理等級](https://platform.claude.com/docs/en/build-with-claude/effort)

## 更新或移除

| 安裝方式 | 更新 | 移除 |
| --- | --- | --- |
| ChatGPT 或 Codex 外掛 | 如果由你管理上傳，請在外掛詳細資料中選擇 **Upload new version**。從目錄或工作區安裝的外掛會從原管道取得更新。 | 開啟 **Plugins → Installed → Game Localization**，若提供 **Uninstall plugin** 則選擇該項。受管理的安裝請洽管理員。 |
| ChatGPT 獨立技能 | 透過技能管理功能，將個人上傳版本替換成最新的獨立技能 ZIP。 | 開啟 **Plugins → Skills**，在 **Installed** 或 **Created by me** 找到技能並選擇可用的移除操作。工作區擁有的技能由管理員管理。 |
| Claude 自訂技能 | 在技能管理頁面上傳新版獨立技能 ZIP。如果出現第二個項目，請停用舊版。 | 在 **Customize → Skills** 或 **Plugins** 開啟技能並停用。若為自己上傳的技能，選擇 **⋯ → Delete** 並確認。 |
| 透過 Skills CLI 安裝的本機技能 | 如有追蹤的分支，執行 `npx skills update game-localization`，也可從新標籤安裝。 | 在同一個專案中執行 `npx skills remove game-localization`。若是全域安裝，請加上 `-g`。 |
| 本機資料夾或 Codex Skill Installer | 將已安裝的 `game-localization/` 資料夾換成最新版。 | 移除已安裝的 `game-localization/`。Codex 可從 `.agents/skills/`、`~/.agents/skills/` 或安裝位置 `~/.codex/skills/` 載入。Claude Code 使用 `.claude/skills/` 或 `~/.claude/skills/`。視需要開啟新工作階段。 |

[管理 OpenAI 外掛](https://learn.chatgpt.com/docs/plugins) · [管理 Claude 自訂技能](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## 原始碼與封裝

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) 定義技能的啟用條件和批次處理方式。
- [`game-localization/references/`](../game-localization/references/) 包含規則及各語言版本的入門詞彙表。
- [`packaging/chatgpt/`](../packaging/chatgpt/) 包含外掛資訊清單與圖示。
- [`packages/`](../packages/) 存放可直接上傳的壓縮檔。

要用同一份原始碼重建兩個 ZIP，請使用 Python 3.9 或更新版本，在儲存庫根目錄執行 `python scripts/package.py`。版本來自 ChatGPT 外掛資訊清單。散布新版前，請將兩個 ZIP 分別上傳至對應產品，並用附有詞彙表和受保護預留位置的小批文字測試。

## 授權條款

Game Localization 採用 [MIT 授權條款](../LICENSE)。Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt)。

## 支持作者

如果 Game Localization 對你的團隊有幫助，歡迎[透過 DonationAlerts 支持 Maled1kt](https://www.donationalerts.com/r/maled1kt)。捐款完全出於自願。
