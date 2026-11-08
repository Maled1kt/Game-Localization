# Game Localization

![여러 언어의 문자를 주고받는 게임 대화창 두 개가 그려진 Game Localization 배너](../assets/game-localization-banner.png)

[English](../README.md) · [모든 언어](../README.md#languages)

Game Localization은 ChatGPT, Codex, Claude에서 게임 텍스트를 번역, 편집, 검토하는 에이전트 스킬입니다. Steam, PlayStation, Xbox 및 모바일 게임의 메뉴, 튜토리얼, 대사, 자막, 스토어 문구, 프로젝트 문서에 사용할 수 있습니다.

[설치](#설치) · [스킬 사용](#스킬-사용) · [업데이트 및 제거](#업데이트-및-제거) · [제작자 후원](#제작자-후원) · [개발 계획](../ROADMAP.md) · [변경 내역](../CHANGELOG.md)

## 주요 기능

- 프로젝트에서 승인한 용어를 적용하고 새 용어는 후보로 기록합니다.
- 현지화 키, `{player_name}` 및 `%s` 같은 자리표시자, 태그, 의미 있는 줄바꿈과 기타 보호 요소를 유지합니다.
- 지정된 길이 제한을 확인하고 번역문과 질문, 원문 수정 사항, 품질 검토 기록을 구분합니다.
- [언어와 지역 변형 30개로 구성된 기본 목록](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages)을 제공하며 사용자 지정 목록도 받습니다.
- [30개 언어 및 지역 변형에 모두 대응하는 75개 기본 용어집](../game-localization/references/glossary/README.md)에 공통 영어 정의와 번역 후보가 들어 있습니다.

스킬에는 지침과 참고 파일이 들어 있습니다. 프로젝트 API 키, 커넥터, 백그라운드 서비스 없이 작동합니다. 파일 편집은 채팅에서 사용할 수 있는 도구에 따라 달라집니다. 출시 전에는 게임 빌드에서 UI 번역을, 플랫폼 미리보기에서 스토어 문구를 확인하세요.

## 설치

| 사용 환경 | 패키지 |
| --- | --- |
| 플러그인 업로드 권한이 있는 ChatGPT 또는 Codex | [ChatGPT 플러그인 ZIP](../packages/game-localization-chatgpt-v0.1.5.zip) |
| Claude 또는 독립 스킬을 업로드할 수 있는 ChatGPT 워크스페이스 | [독립 스킬 ZIP](../packages/game-localization-skill-v0.1.5.zip) |
| 로컬 Codex 또는 Claude Code | [소스 폴더에서 설치](#명령-하나로-로컬-에이전트에-설치) |

GitHub에서 패키지 링크를 열고 **Download raw file**을 선택합니다. ZIP의 압축을 풀지 않고 업로드합니다.

### ChatGPT 및 Codex

1. 웹 ChatGPT에서 계정의 플러그인 업로드 메뉴를 엽니다. 권한이 있는 워크스페이스 소유자와 관리자는 **Admin console → Plugins → Add → Upload plugin**을 사용할 수 있습니다.
2. 플러그인 ZIP을 선택합니다. 검증 후 **Plugins**에서 **Game Localization**을 열고 **Install plugin**이 있으면 선택합니다. 개인 업로드는 **Personal → Created by me**에 표시될 수 있습니다.
3. ChatGPT 또는 Codex에서 새 채팅을 엽니다. `@`를 입력하고 제안 목록에서 **Game Localization**을 선택합니다.

워크스페이스가 독립 스킬을 지원하면 **Plugins → Skills → Create → Upload from your computer**에서 해당 ZIP을 업로드합니다. 검사가 끝나면 안내를 따릅니다. 사용 가능한 옵션은 계정과 워크스페이스에 따라 다릅니다. [OpenAI 플러그인 가이드](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [OpenAI 스킬 가이드](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. 계정이나 워크스페이스에서 요구하는 경우 Claude 설정에서 **Code execution and file creation**을 활성화합니다.
2. 웹 Claude 또는 Claude Desktop에서 **Customize → Skills**를 엽니다. 새 레이아웃에서는 사이드바의 **Plugins**를 열고 **Your plugins**에서 스킬 관리 항목을 찾습니다.
3. **+ → Create skill → Upload a skill**에서 독립 스킬 ZIP을 선택합니다. `game-localization`이 나타나면 활성화합니다.
4. 새 채팅을 열고 Claude에 **Game Localization**을 사용해 달라고 요청합니다. 입력창의 **+** 또는 **/** 메뉴에 스킬이 표시되면 그곳에서 선택합니다.

관리형 워크스페이스에서는 관리자가 스킬을 활성화하거나 업로드해야 할 수 있습니다. [Claude 스킬 가이드](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Claude 사이드바 변경](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### 명령 하나로 로컬 에이전트에 설치

아래 명령은 [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization)의 `main` 브랜치를 사용합니다. 저장소와 브랜치가 공개되면 사용할 수 있습니다. 상대 경로인 ZIP 링크는 다른 브랜치, 태그, 포크에서도 작동합니다.

로컬 Codex 채팅에서 기본 제공 `$skill-installer`를 선택하고 아래 요청을 보냅니다. 필요하면 네트워크 액세스를 승인한 뒤 새 세션을 시작합니다. [Codex 스킬 가이드](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

타사 Skills CLI를 사용하면 터미널 명령 하나로 로컬 Codex와 Claude Code에 같은 소스 폴더를 설치할 수 있습니다. Node.js 22.20 이상으로 대상 프로젝트에서 실행합니다. 필요한 에이전트의 `-a` 옵션만 남깁니다. 사용자 전체에 설치하려면 `-g`를 추가합니다. [Skills CLI 참고 문서](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

로컬 Claude Code 터미널 채팅의 셸 입력에서 Claude 전용 설치를 실행할 수 있습니다. 실행 전 저장소 URL을 확인합니다. [Claude Code 셸 입력](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

새 세션에서 Codex의 `$game-localization` 또는 Claude Code의 `/game-localization`을 호출합니다. Claude Code에 수동 설치하려면 `game-localization/` 폴더 전체를 프로젝트의 `.claude/skills/` 또는 사용자 폴더의 `~/.claude/skills/`에 복사합니다. [Claude Code 스킬 가이드](https://code.claude.com/docs/en/skills)

호스팅된 ChatGPT와 Claude에서는 계정의 업로드 또는 설치 기능을 사용합니다. 채팅 멘션으로 설치된 스킬을 호출합니다. 설치 링크를 공유하려면 플랫폼이 지원하는 디렉터리에 게시하거나 적격 워크스페이스에서 스킬 또는 플러그인을 공유합니다. [ChatGPT 플러그인 공유](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Claude 스킬 공유](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## 스킬 사용

1. 원문 또는 원본 파일과 대상 언어의 최신 프로젝트 용어집을 첨부합니다. 용어집이 없으면 초안을 만들어 달라고 명시합니다.
2. 원본과 대상 로캘, 플랫폼, 콘텐츠 유형 및 출력 형식을 지정합니다. 필요한 경우 글자 수 제한, 화면 캡처, 화자 정보, 변수 예시를 제공합니다.
3. 스프레드시트에서는 원본 열과 대상 열을 지정하고 새 사본을 요청합니다. 게임 문자열에는 고정 ID 또는 키를 제공합니다. 스토어 문구에는 대상 필드와 엄격한 길이 제한이 있다면 함께 적습니다.
4. 별도로 제공되는 인계 문서에서 결과물이 사용 가능한 상태인지, 아직 초안인지 확인합니다. 인계 문서에는 파일 점검, 번역문 검토, 게임 내 또는 스토어 미리보기 확인이 구분되어 있으며, 미해결 문제마다 다음에 할 일이 표시됩니다. 용어는 프로젝트 용어집에서 승인한 후 재사용합니다.

**스프레드시트 프롬프트 예시**

~~~text
Game Localization으로 첨부 통합 문서의 ENGLISH 열을 독일어(de-DE)로 번역해 주세요. 새 .xlsx 사본의 GERMAN 열에 번역문을 넣어 주세요. 첨부 용어집과 DESCRIPTION 열을 참고하고 키, 원본 열, 자리표시자와 태그를 유지해 주세요. 용어 질문과 점검 결과는 행 ID와 함께 별도로 정리해 주세요.
~~~

**스토어 페이지 프롬프트 예시**

~~~text
Game Localization으로 이 Steam 짧은 설명을 영어에서 브라질 포르투갈어(pt-BR)로 현지화해 주세요. 필요하면 용어집 초안을 만들어 주세요. 게임 제목을 유지하고 지정된 글자 수 제한을 지켜 주세요. 스토어 문구와 인계 문서는 따로 주세요.
~~~

### CSV 번역 확인

각 행에 고정 ID가 있는 CSV를 번역할 때는 ID, 원문, 번역문 열의 제목을 지정하세요. Python 3.9 이상을 사용할 수 있으면 스킬이 원문 파일과 번역 파일을 비교해 누락되거나 중복된 ID, 비어 있는 번역, 지원되는 자리표시자나 태그의 변경, 길이 제한 초과를 알려 줍니다. [CSV 확인 안내](../game-localization/references/csv-qa.md)

### 사용하는 모델 설정

| 사용 환경 | 모델 | 추론 수준 |
| --- | --- | --- |
| ChatGPT Work 또는 Codex | GPT-6.1 Sol | High 이상(지원되는 경우) |
| Claude | Claude Opus 5.5 | High 이상(지원되는 경우) |

**High+**는 클라이언트에서 선택할 수 있는 High 이상의 수준을 뜻합니다. 클라이언트에서 모델과 추론 수준을 선택합니다. 스킬은 이 설정과 관계없이 사용할 수 있습니다. [OpenAI 모델 설정](https://learn.chatgpt.com/docs/models) · [Claude 추론 수준](https://platform.claude.com/docs/en/build-with-claude/effort)

## 업데이트 및 제거

| 설치 방식 | 업데이트 | 제거 |
| --- | --- | --- |
| ChatGPT 또는 Codex 플러그인 | 업로드를 관리한다면 상세 화면에서 **Upload new version**을 선택합니다. 디렉터리 또는 워크스페이스 설치는 해당 경로에서 업데이트됩니다. | **Plugins → Installed → Game Localization**에서 **Uninstall plugin**을 선택할 수 있습니다. 관리형 설치는 관리자에게 문의합니다. |
| ChatGPT 독립 스킬 | 스킬 관리 기능에서 개인 업로드를 최신 독립 ZIP으로 바꿉니다. | **Plugins → Skills**의 **Installed** 또는 **Created by me**에서 스킬을 찾아 제거 기능을 사용합니다. 워크스페이스 소유 스킬은 관리자가 관리합니다. |
| Claude 사용자 지정 스킬 | 관리 페이지에서 새 독립 ZIP을 업로드합니다. 항목이 두 개가 되면 이전 버전을 끕니다. | **Customize → Skills** 또는 **Plugins**에서 스킬을 끕니다. 직접 업로드한 스킬은 **⋯ → Delete**를 선택하고 확인합니다. |
| Skills CLI로 설치한 로컬 스킬 | 추적 브랜치에서 `npx skills update game-localization`을 실행하거나 새 태그에서 설치합니다. | 같은 프로젝트에서 `npx skills remove game-localization`을 실행합니다. 전역 설치라면 `-g`를 추가합니다. |
| 로컬 폴더 또는 Codex Skill Installer | 설치된 `game-localization/` 폴더를 최신 버전으로 바꿉니다. | `game-localization/` 폴더를 삭제합니다. Codex는 `.agents/skills/`, `~/.agents/skills/` 또는 `~/.codex/skills/`에서 로드할 수 있습니다. Claude Code는 `.claude/skills/` 또는 `~/.claude/skills/`를 사용합니다. 필요한 경우 새 세션을 시작합니다. |

[OpenAI 플러그인 관리](https://learn.chatgpt.com/docs/plugins) · [Claude 사용자 지정 스킬 관리](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## 소스와 패키지

- [`game-localization/SKILL.md`](../game-localization/SKILL.md)에 스킬의 실행 조건과 일괄 처리 방법이 정의되어 있습니다.
- [`game-localization/references/`](../game-localization/references/)에 규칙과 언어별 기본 용어집이 있습니다.
- [`packaging/chatgpt/`](../packaging/chatgpt/)에 플러그인 매니페스트와 아이콘이 있습니다.
- [`packages/`](../packages/)에 업로드할 압축 파일이 있습니다.

같은 소스에서 두 ZIP을 다시 만들려면 Python 3.9 이상으로 저장소 루트에서 `python scripts/package.py`를 실행합니다. 버전은 ChatGPT 플러그인 매니페스트에서 가져옵니다. 배포 전 각 ZIP을 해당 제품에 업로드하고 용어집과 보호된 자리표시자를 포함한 소량의 텍스트로 테스트합니다.

## 라이선스

Game Localization은 [MIT 라이선스](../LICENSE)로 제공됩니다. Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## 제작자 후원

Game Localization이 팀에 도움이 되었다면 [DonationAlerts에서 Maled1kt를 후원](https://www.donationalerts.com/r/maled1kt)할 수 있습니다. 후원은 자발적입니다.
