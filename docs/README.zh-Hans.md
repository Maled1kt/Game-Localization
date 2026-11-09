# Game Localization

![Game Localization by Maled1kt](../assets/game-localization-banner.png)

[English](../README.md) · [所有语言](../README.md#languages)

Game Localization 是一项代理技能，可在 ChatGPT、Codex 和 Claude 中翻译、编辑和校对游戏文本。适用于 Steam、PlayStation、Xbox 和移动游戏的菜单、教程、对白、字幕、商店文案和项目文档。

[安装](#安装) · [使用技能](#使用技能) · [更新或卸载](#更新或卸载) · [支持作者](#支持作者) · [开发计划](../ROADMAP.md) · [更新日志](../CHANGELOG.md)

## 功能

- 应用项目已批准的术语，将新术语记录为候选项。
- 保留本地化键、`{player_name}` 和 `%s` 等占位符、标签、有意义的换行及其他受保护元素。
- 检查指定的长度限制，将译文与问题、原文修正和质检备注分开交付。
- 提供[包含 30 种语言和地区变体的预设](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages)，也接受自定义列表。
- 内置[覆盖全部 30 种语言和地区变体的 75 词入门术语表](../game-localization/references/glossary/README.md)，包含通用英文定义和候选译法。

技能包含说明和参考文件，无需项目 API 密钥、连接器或后台服务。能否编辑文件取决于聊天中可用的工具。发布前，请在游戏构建版本中检查界面译文，并在平台预览中检查商店文案。

## 安装

| 使用环境 | 安装包 |
| --- | --- |
| 有插件上传权限的 ChatGPT 或 Codex | [ChatGPT 插件 ZIP](../packages/game-localization-chatgpt-v0.1.12.zip) |
| Claude 或允许上传独立技能的 ChatGPT 工作区 | [独立技能 ZIP](../packages/game-localization-skill-v0.1.12.zip) |
| 本地 Codex 或 Claude Code | [从源码文件夹安装](#为本地代理一键安装) |

在本地 Codex 和 Claude Code 中，可以从共用的 GitHub 目录安装 Game Localization。指南介绍首次安装、从 ZIP 版切换以及在各客户端中更新的方法。[GitHub 目录](plugin-catalog.md)

在 GitHub 打开安装包链接并选择 **Download raw file**。上传时保留 ZIP 格式。

### ChatGPT 和 Codex

1. 在 ChatGPT 网页版中打开账户的插件上传入口。有上传权限的工作区所有者和管理员可使用 **Admin console → Plugins → Add → Upload plugin**。
2. 选择插件 ZIP。验证完成后，在 **Plugins** 中打开 **Game Localization**，若提供 **Install plugin** 则选择该项。个人上传内容可能显示在 **Personal → Created by me** 中。
3. 在 ChatGPT 或 Codex 中新建聊天。输入 `@`，从建议中选择 **Game Localization**。

若工作区允许上传独立技能，请在 **Plugins → Skills → Create → Upload from your computer** 上传独立技能 ZIP。等待扫描并按提示操作。可用选项因账户和工作区而异。 [OpenAI 插件指南](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [OpenAI 技能指南](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. 如果账户或工作区有此要求，请在 Claude 设置中启用 **Code execution and file creation**。
2. 在 Claude 网页版或 Claude Desktop 中打开 **Customize → Skills**。在新版界面中，从侧边栏进入 **Plugins**，在 **Your plugins** 下查找技能管理选项。
3. 选择 **+ → Create skill → Upload a skill** 并上传独立技能 ZIP。列表出现 `game-localization` 后将其启用。
4. 新建聊天并请 Claude 使用 **Game Localization**。如果输入区的 **+** 或 **/** 菜单列出了该技能，可直接选择。

在受管理的工作区中，可能需要管理员启用或上传技能。 [Claude 技能指南](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Claude 侧边栏更新](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### 为本地代理一键安装

以下命令使用 [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization) 的 `main` 分支。仓库及分支发布后即可使用。上方 ZIP 链接是相对链接，也适用于其他分支、标签和派生仓库。

在本地 Codex 聊天中选择内置的 `$skill-installer`，发送下面的请求。若系统提示，请允许网络访问，然后开启新会话。 [Codex 技能指南](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

第三方 Skills CLI 可用一条命令为本地 Codex 和 Claude Code 安装同一个源码文件夹。使用 Node.js 22.20 或更高版本，在目标项目中运行命令。只保留所需代理的 `-a` 选项。如需为当前用户全局安装，请加上 `-g`。 [Skills CLI 参考](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

在本地 Claude Code 的终端聊天中，可在 Shell 输入区直接执行仅针对 Claude 的安装。运行前请核对仓库 URL。 [Claude Code Shell 输入](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

开启新会话，在 Codex 中调用 `$game-localization`，或在 Claude Code 中调用 `/game-localization`。如需在 Claude Code 中手动安装，请将完整的 `game-localization/` 文件夹复制到项目的 `.claude/skills/` 或用户的 `~/.claude/skills/`。 [Claude Code 技能指南](https://code.claude.com/docs/en/skills)

使用云端 ChatGPT 或 Claude 时，请通过账户的上传或安装入口操作。在聊天中提及技能即可调用已安装的版本。若要分享安装链接，可发布到平台支持的目录，或在符合条件的工作区分享技能或插件。 [共享 ChatGPT 插件](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [共享 Claude 技能](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## 使用技能

1. 附上源文本或文件，以及目标语言的最新项目术语表。如果没有术语表，请明确要求技能先起草一份。
2. 说明源语言、目标语言、平台、内容类型和交付格式。按需提供字符限制、截图、角色说明或变量示例。
3. 对于电子表格，请指定源列和目标列，并要求另存副本。对于游戏内文本，请提供稳定的 ID 或键。对于商店文案，请注明目标字段和硬性长度限制。
4. 查看单独提供的交付说明，确认结果是可以使用还是仍为草稿。说明分别列出文件检查、译文审校，以及游戏内或商店预览中的检查，并为每个未解决的问题给出下一步。术语应先在项目术语表中确认，再重复使用。

对于游戏界面，交付报告会按优先级列出检查项，包括界面、字符串 ID、复现步骤和通过标准。优先检查较长的变量替换值和可能被截断的文字。如果已知字体和文字可用宽度，技能可以估算所需空间。[游戏内检查指南](../game-localization/references/in-build-qa.md)

使用[项目术语表模板](../game-localization/references/project-glossary-template.md)分别记录已确认的术语和候选术语。保存更新后的文件，并在下次聊天时将其附上。

**电子表格提示词示例**

~~~text
使用 Game Localization 将附件工作簿的 ENGLISH 列译成德语（de-DE），把译文写入新 .xlsx 副本的 GERMAN 列。参考附带的术语表和 DESCRIPTION 列。保留键、源列、占位符及标签。另列术语问题和检查结果，并标注行 ID。
~~~

对于受支持的 `.xlsx` 文件，请指定工作表、表头行、包含固定 ID 的列、源列和现有的目标列。在 Python 3.9 或更高版本中，技能会按 ID 将译文写入新副本，并检查工作簿其余部分是否保留。如果无法验证工作簿，技能可以提供包含 ID 的 CSV。[Excel 使用说明](../game-localization/references/xlsx-qa.md)

**商店页面提示词示例**

~~~text
使用 Game Localization 将这段 Steam 简短描述从英语本地化为巴西葡萄牙语（pt-BR）。如有需要，先起草术语表。保留游戏名称并遵守给定的字符限制。分别提交商店文案和交付说明。
~~~

处理 Steam 商店页面时，技能会分别交付简短描述和“关于这款游戏”，检查指定限制及有关游戏的陈述，并可从受支持的 Steamworks JSON 导出文件生成草稿。交付报告会分别记录导入和预览状态。[Steam 商店页面工作流程](../game-localization/references/steam-store.md)

### 检查 CSV 译文

如果 CSV 中的每行都有固定 ID，请指定 ID、原文和译文所在的列名。环境支持 Python 3.9 或更高版本时，技能会比对原文文件和译文文件，报告缺失或重复的 ID、空白译文、受支持的占位符或标签发生的改动，以及超出长度限制的条目。 [CSV 检查说明](../game-localization/references/csv-qa.md)

更新译文时，请附上旧版和当前版源 CSV、已确认的译文以及后续编辑改动。技能会按 ID 匹配行，保留未改动行中仍可使用的译文，并标出新增、修改和删除的行。处理长对话时，请在每个场景结束后保存进度，以便用同一份工作文件继续。[更新 CSV 译文](../game-localization/references/csv-updates.md)

试试[包含 12 行文本的入门示例](../game-localization/examples/first-run/README.md)，其中附有译文草稿、已确认的术语表和交付说明样例。

### 我们的模型设置

| 使用环境 | 模型 | 推理级别 |
| --- | --- | --- |
| ChatGPT Work 或 Codex | GPT-6.1 Sol | High 或更高（视可用选项而定） |
| Claude | Claude Opus 5.5 | High 或更高（视可用选项而定） |

**High+** 指客户端提供的 High 或更高推理级别。请在客户端选择模型和级别。技能可在不同级别下使用。 [OpenAI 模型设置](https://learn.chatgpt.com/docs/models) · [Claude 推理级别](https://platform.claude.com/docs/en/build-with-claude/effort)

## 更新或卸载

| 安装方式 | 更新 | 卸载 |
| --- | --- | --- |
| ChatGPT 或 Codex 插件 | 如果由你管理上传，请在插件详情选择 **Upload new version**。通过目录或工作区安装的插件从原渠道获取更新。 | 打开 **Plugins → Installed → Game Localization**，若提供 **Uninstall plugin** 则选择该项。受管理的安装请联系管理员。 |
| ChatGPT 独立技能 | 使用技能管理功能，将个人上传的版本替换为最新的独立技能 ZIP。 | 打开 **Plugins → Skills**，在 **Installed** 或 **Created by me** 中找到技能并选择可用的移除操作。工作区管理员负责管理工作区所有的技能。 |
| Claude 自定义技能 | 从技能管理页面上传新版独立技能 ZIP。如果出现第二个条目，请停用旧版。 | 在 **Customize → Skills** 或 **Plugins** 中找到技能并停用。对于自己上传的技能，选择 **⋯ → Delete** 并确认。 |
| 通过 Skills CLI 安装的本地技能 | 跟踪分支时运行 `npx skills update game-localization`，也可从新标签安装。 | 在同一项目中运行 `npx skills remove game-localization`。如果是全局安装，请加上 `-g`。 |
| 本地文件夹或 Codex Skill Installer | 用最新版替换已安装的 `game-localization/` 文件夹。 | 移除已安装的 `game-localization/`。Codex 可从 `.agents/skills/`、`~/.agents/skills/` 或安装位置 `~/.codex/skills/` 加载。Claude Code 使用 `.claude/skills/` 或 `~/.claude/skills/`。如有需要，开启新会话。 |

[管理 OpenAI 插件](https://learn.chatgpt.com/docs/plugins) · [管理 Claude 自定义技能](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## 源码与打包

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) 定义技能的触发条件和批量处理方式。
- [`game-localization/references/`](../game-localization/references/) 包含规则以及各语言的入门术语表。
- [`packaging/chatgpt/`](../packaging/chatgpt/) 包含插件清单和图标。
- [`packages/`](../packages/) 存放可直接上传的压缩包。

要从同一源码重建两个 ZIP，请使用 Python 3.9 或更高版本，在仓库根目录执行 `python scripts/package.py`。版本号来自 ChatGPT 插件清单。分发新版本前，请在对应产品中分别上传两个 ZIP，并用带有术语表和受保护占位符的小批量文本进行测试。

## 许可证

Game Localization 根据 [MIT 许可证](../LICENSE)发布。Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt)。

## 支持作者

如果 Game Localization 对你的团队有帮助，欢迎[通过 DonationAlerts 支持 Maled1kt](https://www.donationalerts.com/r/maled1kt)。捐赠完全自愿。
