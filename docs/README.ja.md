# Game Localization

![Game Localization by Maled1kt](../assets/game-localization-banner.png)

[English](../README.md) · [すべての言語](../README.md#languages)

Game Localization は、ChatGPT、Codex、Claude でゲームテキストを翻訳・編集・レビューするためのエージェントスキルです。Steam、PlayStation、Xbox、モバイルゲームのメニュー、チュートリアル、会話、字幕、ストア文面、プロジェクト文書に対応します。

[インストール](#インストール) · [スキルの使い方](#スキルの使い方) · [更新と削除](#更新と削除) · [作者を支援する](#作者を支援する) · [開発計画](../ROADMAP.md) · [変更履歴](../CHANGELOG.md)

## 機能

- プロジェクトで承認された用語を適用し、新しい用語は候補として記録します。
- ローカライズキー、`{player_name}` や `%s` などのプレースホルダー、タグ、意味のある改行、その他の保護対象を保持します。
- 指定の長さ制限を確認し、訳文と質問、原文の修正案、品質チェックの所見を分けて返します。
- [30件の言語・ロケールのプリセット](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages)のほか、独自の一覧を指定できます。
- [全30言語・ロケールに対応する75語のスターター用語集](../game-localization/references/glossary/README.md)が付属します。英語の共通定義と訳語候補を収録しています。

スキルは手順と参照ファイルで構成され、プロジェクトのAPIキー、コネクター、バックグラウンドサービスは不要です。ファイルを編集できるかどうかはチャットで利用できるツールによります。リリース前に、UIの訳文はゲームビルドで、ストア文面はプラットフォームのプレビューで確認してください。

## インストール

| 利用環境 | パッケージ |
| --- | --- |
| プラグインのアップロード権限がある ChatGPT または Codex | [ChatGPT プラグインの ZIP](../packages/game-localization-chatgpt-v0.1.8.zip) |
| Claude または単体スキルのアップロードに対応する ChatGPT ワークスペース | [単体スキルの ZIP](../packages/game-localization-skill-v0.1.8.zip) |
| ローカルの Codex または Claude Code | [ソースフォルダーからインストール](#ローカルエージェントに1コマンドでインストール) |

GitHub でパッケージのリンクを開き、**Download raw file** を選択します。ZIP は展開せずにアップロードしてください。

### ChatGPT と Codex

1. Web 版 ChatGPT でアカウントのプラグインアップロード画面を開きます。権限があるワークスペース所有者と管理者は **Admin console → Plugins → Add → Upload plugin** を使用できます。
2. プラグインの ZIP を選びます。検証後、**Plugins** で **Game Localization** を開き、**Install plugin** が表示されていれば選びます。個人でアップロードしたものは **Personal → Created by me** に表示される場合があります。
3. ChatGPT または Codex で新しいチャットを開きます。`@` と入力し、候補から **Game Localization** を選びます。

ワークスペースが単体スキルに対応していれば、**Plugins → Skills → Create → Upload from your computer** で単体スキルの ZIP をアップロードします。スキャンが終わったら画面の案内に従います。利用できる選択肢はアカウントとワークスペースによります。 [OpenAI プラグインガイド](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [OpenAI スキルガイド](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. アカウントまたはワークスペースで必要な場合は、Claude の設定で **Code execution and file creation** を有効にします。
2. Web 版 Claude または Claude Desktop で **Customize → Skills** を開きます。新しい画面ではサイドバーの **Plugins** を開き、**Your plugins** にあるスキル管理項目を探します。
3. **+ → Create skill → Upload a skill** で単体スキルの ZIP を選び、`game-localization` が表示されたら有効にします。
4. 新しいチャットを開き、Claude に **Game Localization** を使うよう依頼します。入力欄の **+** または **/** に表示される場合は、そこから選べます。

管理対象のワークスペースでは、管理者によるスキルの有効化やアップロードが必要な場合があります。 [Claude スキルガイド](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Claude の新しいサイドバー](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### ローカルエージェントに1コマンドでインストール

以下のコマンドは [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization) の `main` ブランチを使用します。リポジトリとブランチの公開後に利用できます。上の ZIP リンクは相対パスなので、別のブランチ、タグ、フォークでも機能します。

ローカルの Codex チャットで組み込みの `$skill-installer` を選び、次のリクエストを送ります。求められたらネットワークアクセスを許可し、新しいセッションを開始します。 [Codex スキルガイド](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

サードパーティーの Skills CLI では、ローカルの Codex と Claude Code の両方に同じソースフォルダーを1コマンドでインストールできます。Node.js 22.20 以降を使い、対象プロジェクトで実行します。必要なエージェントの `-a` だけを残します。ユーザー全体にインストールする場合は `-g` を付けます。 [Skills CLI リファレンス](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

ローカルの Claude Code のターミナルチャットでは、シェル入力で Claude のみにインストールできます。実行前にリポジトリの URL を確認します。 [Claude Code のシェル入力](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

新しいセッションで Codex なら `$game-localization`、Claude Code なら `/game-localization` を呼び出します。Claude Code に手動で追加するには、`game-localization/` フォルダー全体をプロジェクトの `.claude/skills/` またはユーザーの `~/.claude/skills/` にコピーします。 [Claude Code スキルガイド](https://code.claude.com/docs/en/skills)

ホスト版の ChatGPT と Claude では、アカウントのアップロードまたはインストール機能を使います。チャットでメンションするとインストール済みのスキルを呼び出せます。共有用のインストールリンクが必要なら、対応するプラットフォームのディレクトリに公開するか、対象ワークスペースでスキルやプラグインを共有します。 [ChatGPT プラグインの共有](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Claude スキルの共有](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## スキルの使い方

1. 原文または元ファイルと、対象言語の最新プロジェクト用語集を添付します。用語集がなければ、草案の作成を明示的に依頼します。
2. 原文と訳文のロケール、プラットフォーム、素材の種類、出力形式を指定します。必要に応じて文字数制限、スクリーンショット、話者情報、変数の例も添えます。
3. 表では原文と訳文の列を指定し、新しいコピーを依頼します。ゲーム内テキストでは固定の ID やキーを、ストア文面では対象項目と厳密な長さ制限があればそれを伝えます。
4. 結果が利用可能か、まだ下書きの段階かを、別に用意される引き継ぎメモで確認します。メモにはファイルのチェック、訳文のレビュー、ゲーム内またはストアプレビューでの確認の状況が個別に記載され、未解決の問題ごとに次の対応が示されます。用語はプロジェクト用語集で承認してから再利用します。

[プロジェクト用語集のテンプレート](../game-localization/references/project-glossary-template.md)で、承認済みの用語と候補を分けて管理します。更新したファイルを保存し、次のチャットに添付してください。

**スプレッドシート用プロンプト例**

~~~text
Game Localization を使って添付のブックの ENGLISH 列をドイツ語（de-DE）に訳してください。新しい .xlsx コピーの GERMAN 列に訳文を入れ、添付の用語集と DESCRIPTION 列を参照してください。キー、原文列、プレースホルダー、タグを保持し、用語の質問とチェック結果は行 ID を添えて別にまとめてください。
~~~

対応する `.xlsx` ファイルでは、シート名、見出し行、固定の行 ID が入った列、原文列、既存の翻訳先列を指定してください。Python 3.9 以降が使える場合、スキルは ID で行を照合して新しいコピーに訳文を書き込み、ブックの他の部分が保持されているかを確認します。ブックを確認できない場合は、ID 付きの CSV を提示できます。[Excel の手順](../game-localization/references/xlsx-qa.md)

**ストアページ用プロンプト例**

~~~text
Game Localization を使って、この Steam の短い説明文を英語からブラジルポルトガル語（pt-BR）にローカライズしてください。必要なら用語集の草案を作ってください。ゲームタイトルはそのままにし、指定の文字数制限を守ってください。ストア文面と引き継ぎメモは分けて返してください。
~~~

### CSV翻訳をチェックする

各行に固定のIDがあるCSVでは、ID、原文、訳文の列見出しを指定してください。Python 3.9以降を利用できる環境では、スキルが原文ファイルと翻訳ファイルを比較し、IDの欠落や重複、訳文の空欄、対応するプレースホルダーやタグの変更、長さ制限の超過を報告します。 [CSVチェックの手順](../game-localization/references/csv-qa.md)

[12行の入門サンプル](../game-localization/examples/first-run/README.md)では、翻訳の下書き、承認済みの用語集、引き継ぎメモの例を使って、スキルを試せます。

### 使用しているモデル設定

| 利用環境 | モデル | 推論レベル |
| --- | --- | --- |
| ChatGPT Work または Codex | GPT-6.1 Sol | High 以上（利用可能な場合） |
| Claude | Claude Opus 5.5 | High 以上（利用可能な場合） |

**High+** は、クライアントで選べる High 以上の設定を指します。モデルと推論レベルはクライアントで選択してください。スキルはこの設定にかかわらず使えます。 [OpenAI モデル設定](https://learn.chatgpt.com/docs/models) · [Claude の推論レベル](https://platform.claude.com/docs/en/build-with-claude/effort)

## 更新と削除

| インストール方式 | 更新 | 削除 |
| --- | --- | --- |
| ChatGPT または Codex のプラグイン | アップロードを管理している場合は、詳細画面で **Upload new version** を選びます。ディレクトリやワークスペース経由の更新はその配布元から届きます。 | **Plugins → Installed → Game Localization** を開き、**Uninstall plugin** があれば選びます。管理対象のインストールは管理者に問い合わせてください。 |
| ChatGPT の単体スキル | スキル管理画面で、個人のアップロードを最新の単体スキルの ZIP に置き換えます。 | **Plugins → Skills** の **Installed** または **Created by me** でスキルを探し、利用できる削除操作を使います。ワークスペース所有のスキルは管理者が管理します。 |
| Claude のカスタムスキル | 管理画面から新しい単体スキルの ZIP をアップロードします。別項目が追加されたら旧版を無効にします。 | **Customize → Skills** または **Plugins** で無効にします。自分でアップロードしたスキルは **⋯ → Delete** を選び、確定します。 |
| Skills CLI でインストールしたローカルスキル | 追跡中のブランチなら `npx skills update game-localization` を実行します。新しいタグからのインストールも可能です。 | 同じプロジェクトで `npx skills remove game-localization` を実行します。グローバルにインストールした場合は `-g` を付けます。 |
| ローカルフォルダーまたは Codex Skill Installer | インストール済みの `game-localization/` フォルダーを最新版に置き換えます。 | インストール済みの `game-localization/` を削除します。Codex の読み込み先は `.agents/skills/`、`~/.agents/skills/`、インストーラーの `~/.codex/skills/` です。Claude Code は `.claude/skills/` または `~/.claude/skills/` を使います。必要に応じて新しいセッションを開始します。 |

[OpenAI プラグイン管理](https://learn.chatgpt.com/docs/plugins) · [Claude カスタムスキル管理](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## ソースとパッケージ

- [`game-localization/SKILL.md`](../game-localization/SKILL.md)にはスキルの起動条件とバッチ処理の手順が記載されています。
- [`game-localization/references/`](../game-localization/references/)にはルールと言語別のスターター用語集があります。
- [`packaging/chatgpt/`](../packaging/chatgpt/)にはプラグインのマニフェストとアイコンがあります。
- [`packages/`](../packages/)にはアップロード用のアーカイブがあります。

同じソースから両方の ZIP を再構築するには、Python 3.9 以降でリポジトリのルートから `python scripts/package.py` を実行します。バージョンは ChatGPT プラグインのマニフェストに従います。配布前に各 ZIP を対象製品にアップロードし、用語集と保護対象のプレースホルダーを含む少量のテキストで試してください。

## ライセンス

Game Localization は [MIT ライセンス](../LICENSE)で提供されます。Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt)。

## 作者を支援する

Game Localization がチームの役に立ったら、[DonationAlerts で Maled1kt を支援](https://www.donationalerts.com/r/maled1kt)できます。寄付は任意です。
