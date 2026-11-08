# Game Localization

![Game-Localization-Banner mit zwei Spieldialogen, die Schriftzeichen verschiedener Sprachen austauschen](../assets/game-localization-banner.png)

[English](../README.md) · [Alle Sprachen](../README.md#languages)

Game Localization ist ein Agent Skill zum Übersetzen, Bearbeiten und Prüfen von Videospieltexten in ChatGPT, Codex und Claude. Er unterstützt Menüs, Tutorials, Dialoge, Untertitel, Shoptexte und Projektdokumentation für Steam, PlayStation, Xbox und Mobile-Spiele.

[Installation](#installation) · [Skill verwenden](#skill-verwenden) · [Aktualisieren oder entfernen](#aktualisieren-oder-entfernen) · [Autor unterstützen](#autor-unterstützen) · [Entwicklungsplan](../ROADMAP.md) · [Änderungsprotokoll](../CHANGELOG.md)

## Funktionen

- Wendet freigegebene Projektterminologie an und erfasst neue Begriffe als Vorschläge.
- Erhält Lokalisierungsschlüssel, Platzhalter wie `{player_name}` und `%s`, Tags, relevante Zeilenumbrüche und andere geschützte Elemente.
- Prüft Längenlimits und trennt Übersetzungen von Rückfragen, Quelltextkorrekturen und Hinweisen zur Qualitätssicherung.
- Bietet eine [Vorauswahl mit 30 Sprachen und Sprachvarianten](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages) und akzeptiert eigene Listen.
- Enthält ein [Startglossar mit 75 Begriffen in allen 30 Sprachen und Sprachvarianten](../game-localization/references/glossary/README.md), mit gemeinsamen englischen Definitionen und Übersetzungsvorschlägen.

Der Skill besteht aus Anleitungen und Referenzdateien. Er benötigt keinen Projekt-API-Schlüssel, Connector oder Hintergrunddienst. Die Dateibearbeitung hängt von den Chatwerkzeugen ab. Prüfe vor der Freigabe die Oberfläche im Spielbuild und Shoptexte in der Plattformvorschau.

## Installation

| Umgebung | Paket |
| --- | --- |
| ChatGPT oder Codex mit Plugin-Upload-Berechtigung | [ZIP für das ChatGPT-Plugin](../packages/game-localization-chatgpt-v0.1.4.zip) |
| Claude oder berechtigte ChatGPT-Workspaces mit separatem Skill-Upload | [ZIP für den eigenständigen Skill](../packages/game-localization-skill-v0.1.4.zip) |
| Lokaler Codex oder Claude Code | [Installation aus dem Quellordner](#installation-für-lokale-agenten-mit-einem-befehl) |

Öffne den Paketlink auf GitHub und wähle **Download raw file**. Lade das ZIP ungeöffnet hoch.

### ChatGPT und Codex

1. Öffne den Plugin-Upload in ChatGPT im Web. Workspace-Inhaber und berechtigte Administratoren können **Admin console → Plugins → Add → Upload plugin** verwenden.
2. Wähle das Plugin-ZIP. Öffne nach der Prüfung **Game Localization** unter **Plugins** und wähle **Install plugin**, falls angeboten. Persönliche Uploads können unter **Personal → Created by me** erscheinen.
3. Starte einen neuen Chat in ChatGPT oder Codex. Gib `@` ein und wähle **Game Localization** aus.

Falls der Workspace eigenständige Skills unterstützt, lade das Skill-ZIP über **Plugins → Skills → Create → Upload from your computer** hoch. Warte auf die Prüfung und folge den Hinweisen. Die Optionen hängen vom Konto und Workspace ab. [OpenAI-Plugin-Anleitung](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [OpenAI-Skill-Anleitung](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. Aktiviere **Code execution and file creation** in den Claude-Einstellungen, falls dein Konto oder Workspace dies verlangt.
2. Öffne in Claude im Web oder in Claude Desktop **Customize → Skills**. Im neuen Layout findest du die Einstellungen unter **Plugins** in der Seitenleiste und dann **Your plugins**.
3. Wähle **+ → Create skill → Upload a skill** und das eigenständige Skill-ZIP. Aktiviere `game-localization`, sobald der Skill erscheint.
4. Starte einen neuen Chat und bitte Claude, **Game Localization** zu verwenden. Falls der Skill unter **+** oder **/** erscheint, wähle ihn dort aus.

In verwalteten Workspaces muss ein Administrator Skills unter Umständen aktivieren oder hochladen. [Claude-Skill-Anleitung](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Neue Claude-Seitenleiste](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### Installation für lokale Agenten mit einem Befehl

Die Befehle verwenden den Branch `main` von [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization). Sie funktionieren nach Veröffentlichung des Repositorys und Branches. Die relativen ZIP-Links funktionieren auch in anderen Branches, Tags und Forks.

Wähle im lokalen Codex-Chat `$skill-installer` und sende die Anfrage unten. Erlaube bei Bedarf den Netzwerkzugriff und starte eine neue Sitzung. [Codex-Skill-Anleitung](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

Das externe Skills CLI installiert denselben Quellordner für lokalen Codex und Claude Code mit einem Terminalbefehl. Führe ihn mit Node.js 22.20 oder neuer im Zielprojekt aus. Behalte die benötigten `-a`-Optionen. Ergänze `-g` für eine benutzerweite Installation. [Skills-CLI-Referenz](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

Verwende im lokalen Terminalchat von Claude Code die Shell-Eingabe für die Installation nur in Claude. Prüfe vorher die Repository-URL. [Shell-Eingabe in Claude Code](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

Rufe in einer neuen Sitzung `$game-localization` in Codex oder `/game-localization` in Claude Code auf. Kopiere bei manueller Installation den vollständigen Ordner `game-localization/` nach `.claude/skills/` im Projekt oder nach `~/.claude/skills/` im Benutzerverzeichnis. [Claude-Code-Skill-Anleitung](https://code.claude.com/docs/en/skills)

Verwende im gehosteten ChatGPT und Claude die Upload- oder Installationsoptionen des Kontos. Eine Erwähnung ruft den installierten Skill auf. Für einen teilbaren Installationslink nutze den Plattformkatalog oder teile den Skill oder das Plugin in einem berechtigten Workspace. [ChatGPT-Plugins teilen](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Claude-Skills teilen](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Skill verwenden

1. Hänge die Quelle und das Projektglossar für die Zielsprachen an. Falls es kein Glossar gibt, bitte ausdrücklich um einen Entwurf.
2. Gib Quell- und Zielsprachen, Plattform, Textsorte und Ausgabeformat an. Ergänze bei Bedarf Zeichenlimits, Screenshots, Sprecherhinweise oder Variablenbeispiele.
3. Nenne bei Tabellen Quell- und Zielspalten und bitte um eine neue Kopie. Gib für Spieltexte stabile IDs oder Schlüssel an. Nenne für Shoptexte das Zielfeld und etwaige feste Längenlimits.
4. Prüfe im Übergabebericht offene Zeilen, vorläufige Begriffe und abgeschlossene Prüfungen. Gib Begriffe vor der Wiederverwendung im Projektglossar frei und prüfe den Text im Build oder in der Shopvorschau.

**Beispiel für Tabellen**

~~~text
Übersetze mit Game Localization die Spalte ENGLISH der angehängten Arbeitsmappe ins Deutsche (de-DE). Schreibe die Übersetzungen in GERMAN in einer neuen .xlsx-Kopie. Verwende das Glossar und die Spalte DESCRIPTION als Kontext. Erhalte Schlüssel, Quellspalten, Platzhalter und Tags. Liste Terminologiefragen und Prüfungen separat mit Zeilen-IDs auf.
~~~

**Beispiel für Shopseiten**

~~~text
Lokalisiere mit Game Localization diese Steam-Kurzbeschreibung aus dem Englischen ins brasilianische Portugiesisch (pt-BR). Beginne bei Bedarf mit einem Glossarentwurf. Erhalte den Spieltitel und halte das angegebene Zeichenlimit ein. Gib den Shoptext und einen separaten Übergabebericht aus.
~~~

### CSV-Übersetzungen prüfen

Gib bei einer CSV-Datei mit stabilen Zeilen-IDs die Spaltenüberschriften für ID, Quelltext und Übersetzung an. Wenn Python 3.9 oder neuer verfügbar ist, vergleicht der Skill die Quelldatei mit der übersetzten Datei und meldet fehlende oder doppelte IDs, leere Übersetzungen, Änderungen an unterstützten Platzhaltern oder Tags und überschrittene Längenlimits. [Anleitung zur CSV-Prüfung](../game-localization/references/csv-qa.md)

### Unsere Modelleinstellungen

| Umgebung | Modell | Reasoning-Stufe |
| --- | --- | --- |
| ChatGPT Work oder Codex | GPT-6.1 Sol | High oder höher, falls verfügbar |
| Claude | Claude Opus 5.5 | High oder höher, falls verfügbar |

**High+** steht für High oder eine höhere im Client verfügbare Stufe. Wähle Modell und Stufe im Client. Der Skill funktioniert unabhängig von dieser Einstellung. [OpenAI-Modelleinstellungen](https://learn.chatgpt.com/docs/models) · [Claude-Reasoning-Stufen](https://platform.claude.com/docs/en/build-with-claude/effort)

## Aktualisieren oder entfernen

| Installation | Aktualisieren | Entfernen |
| --- | --- | --- |
| ChatGPT- oder Codex-Plugin | Wähle **Upload new version** in den Plugin-Details, wenn du den Upload verwaltest. Installationen aus einem Katalog oder Workspace beziehen Updates von dort. | Öffne **Plugins → Installed → Game Localization** und wähle **Uninstall plugin**, falls verfügbar. Frage bei verwalteten Installationen den Administrator. |
| Eigenständiger ChatGPT-Skill | Ersetze den persönlichen Upload in der Skill-Verwaltung durch das aktuelle eigenständige ZIP. | Suche unter **Plugins → Skills** in **Installed** oder **Created by me** und verwende die Option zum Entfernen. Workspace-Administratoren verwalten die Skills des Workspace. |
| Benutzerdefinierter Claude-Skill | Lade das neue eigenständige ZIP in der Skill-Verwaltung hoch. Deaktiviere den alten Eintrag, falls ein zweiter entsteht. | Öffne den Skill unter **Customize → Skills** oder **Plugins** und deaktiviere ihn. Wähle bei einem eigenen Upload **⋯ → Delete** und bestätige. |
| Lokaler Skill aus dem Skills CLI | Führe für einen verfolgten Branch `npx skills update game-localization` aus oder installiere vom neuen Tag. | Führe im selben Projekt `npx skills remove game-localization` aus. Ergänze `-g` bei globaler Installation. |
| Lokaler Ordner oder Codex Skill Installer | Ersetze den Ordner `game-localization/` durch die aktuelle Version. | Entferne `game-localization/`. Codex lädt den Ordner aus `.agents/skills/`, `~/.agents/skills/` oder `~/.codex/skills/`. Claude Code verwendet `.claude/skills/` oder `~/.claude/skills/`. Starte bei Bedarf eine neue Sitzung. |

[OpenAI-Plugins verwalten](https://learn.chatgpt.com/docs/plugins) · [Claude-Skills verwalten](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Quellcode und Pakete

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) bestimmt, wann der Skill startet und wie er Textpakete verarbeitet.
- [`game-localization/references/`](../game-localization/references/) enthält Regeln und Sprachversionen des Startglossars.
- [`packaging/chatgpt/`](../packaging/chatgpt/) enthält das Manifest und Symbol des Plugins.
- [`packages/`](../packages/) enthält die Archive für den Upload.

Erstelle beide ZIP-Dateien aus derselben Quelle mit `python scripts/package.py` im Repository-Stammverzeichnis und Python 3.9 oder neuer. Die Version stammt aus dem ChatGPT-Plugin-Manifest. Lade vor der Verteilung beide Archive im jeweiligen Produkt hoch und teste einen kleinen Textsatz mit Glossar und geschütztem Platzhalter.

## Lizenz

Game Localization steht unter der [MIT-Lizenz](../LICENSE). Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## Autor unterstützen

Wenn Game Localization deinem Team hilft, kannst du [Maled1kt über DonationAlerts unterstützen](https://www.donationalerts.com/r/maled1kt). Spenden sind freiwillig.
