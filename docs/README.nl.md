# Game Localization

![Game Localization-banner met twee speldialogen die tekens uit verschillende talen uitwisselen](../assets/game-localization-banner.png)

[English](../README.md) · [Alle talen](../README.md#languages)

Game Localization is een agentskill voor het vertalen, bewerken en controleren van gameteksten in ChatGPT, Codex en Claude. De skill ondersteunt menu’s, tutorials, dialogen, ondertiteling, winkelteksten en projectdocumentatie voor Steam, PlayStation, Xbox en mobiele games.

[Installatie](#installatie) · [De skill gebruiken](#de-skill-gebruiken) · [Bijwerken of verwijderen](#bijwerken-of-verwijderen) · [De maker steunen](#de-maker-steunen) · [Ontwikkelplan](../ROADMAP.md) · [Wijzigingslogboek](../CHANGELOG.md)

## Functies

- Past goedgekeurde projectterminologie toe en legt nieuwe termen vast als voorstellen.
- Behoudt lokalisatiesleutels, tijdelijke aanduidingen zoals `{player_name}` en `%s`, tags, betekenisvolle regeleinden en andere beschermde elementen.
- Controleert lengtelimieten en houdt vertalingen gescheiden van vragen, broncorrecties en opmerkingen over kwaliteitscontrole.
- Biedt een [vooraf ingestelde lijst van 30 talen en varianten](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages) en ondersteunt eigen lijsten.
- Bevat een [startwoordenlijst van 75 termen voor alle 30 talen en varianten](../game-localization/references/glossary/README.md), met gedeelde Engelse definities en vertaalvoorstellen.

De skill bevat instructies en referentiebestanden. Een project-API-sleutel, connector of achtergronddienst is niet nodig. Of je bestanden kunt bewerken, hangt af van de beschikbare chattools. Controleer voor release de vertaalde interface in de gamebuild en winkelteksten in de platformpreview.

## Installatie

| Omgeving | Pakket |
| --- | --- |
| ChatGPT of Codex met rechten om plug-ins te uploaden | [ZIP voor de ChatGPT-plug-in](../packages/game-localization-chatgpt-v0.1.6.zip) |
| Claude of ChatGPT-werkruimten die losse skills mogen uploaden | [ZIP voor de losse skill](../packages/game-localization-skill-v0.1.6.zip) |
| Lokale Codex of Claude Code | [Installeren vanuit de bronmap](#lokale-agents-installeren-met-één-opdracht) |

Open de pakketlink op GitHub en kies **Download raw file**. Upload het ZIP-bestand zonder het uit te pakken.

### ChatGPT en Codex

1. Open in ChatGPT op het web de uploadoptie voor je account. Werkruimte-eigenaren en bevoegde beheerders kunnen **Admin console → Plugins → Add → Upload plugin** gebruiken.
2. Selecteer de plug-in-ZIP. Open na validatie **Game Localization** onder **Plugins** en kies **Install plugin** als dit beschikbaar is. Persoonlijke uploads kunnen onder **Personal → Created by me** staan.
3. Open een nieuwe chat in ChatGPT of Codex. Typ `@` en kies **Game Localization** uit de suggesties.

Als je werkruimte losse skills ondersteunt, upload je de skill-ZIP via **Plugins → Skills → Create → Upload from your computer**. Wacht op de scan en volg de aanwijzingen. De opties hangen af van je account en werkruimte. [OpenAI-handleiding voor plug-ins](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [OpenAI-handleiding voor skills](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. Schakel **Code execution and file creation** in bij Claude als je account of werkruimte dit vereist.
2. Open **Customize → Skills** in Claude op het web of Claude Desktop. Open in de nieuwe indeling **Plugins** in de zijbalk en zoek de bediening onder **Your plugins**.
3. Kies **+ → Create skill → Upload a skill** en selecteer de losse skill-ZIP. Schakel `game-localization` in zodra die verschijnt.
4. Open een nieuwe chat en vraag Claude om **Game Localization** te gebruiken. Verschijnt de skill onder **+** of **/** in het invoerveld, selecteer die dan daar.

In beheerde werkruimten moet een beheerder skills mogelijk inschakelen of uploaden. [Claude-handleiding voor skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Nieuwe Claude-zijbalk](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### Lokale agents installeren met één opdracht

De opdrachten gebruiken de `main`-branch van [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization). Ze werken zodra de repository en branch zijn gepubliceerd. De relatieve ZIP-links werken ook op andere branches, tags en forks.

Selecteer in een lokale Codex-chat `$skill-installer` en stuur het verzoek hieronder. Sta zo nodig netwerktoegang toe en start daarna een nieuwe sessie. [Codex-handleiding voor skills](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

De externe Skills CLI installeert dezelfde bronmap voor lokale Codex en Claude Code in één opdracht. Voer de opdracht uit in het gewenste project met Node.js 22.20 of hoger. Behoud alleen de benodigde `-a`-opties. Voeg `-g` toe voor installatie op gebruikersniveau. [Skills CLI-referentie](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

Gebruik in de lokale terminalchat van Claude Code de shellinvoer om de skill alleen voor Claude te installeren. Controleer vooraf de repository-URL. [Shellinvoer in Claude Code](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

Roep in een nieuwe sessie `$game-localization` aan in Codex of `/game-localization` in Claude Code. Kopieer voor handmatige installatie de volledige map `game-localization/` naar `.claude/skills/` in het project of `~/.claude/skills/` voor je gebruiker. [Claude Code-handleiding voor skills](https://code.claude.com/docs/en/skills)

Gebruik in de gehoste versies van ChatGPT en Claude de upload- of installatieopties van je account. Een vermelding roept een geïnstalleerde skill aan. Voor een deelbare installatielink kun je publiceren via de ondersteunde catalogus of de skill of plug-in delen in een geschikte werkruimte. [ChatGPT-plug-ins delen](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Claude-skills delen](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## De skill gebruiken

1. Voeg de brontekst of het bestand en de actuele projectwoordenlijst voor de doeltalen toe. Vraag expliciet om een concept als er geen woordenlijst is.
2. Geef bron- en doeltaal, platform, materiaalsoort en uitvoerformaat op. Voeg zo nodig tekenlimieten, schermafbeeldingen, informatie over sprekers of variabelevoorbeelden toe.
3. Noem bij een spreadsheet de bron- en doelkolommen en vraag om een nieuwe kopie. Geef voor gameteksten stabiele ID’s of sleutels op. Vermeld voor winkelteksten het doelveld en een eventuele harde lengtelimiet.
4. Lees in het afzonderlijke overdrachtsverslag of het resultaat klaar is voor gebruik of nog een concept is. Het verslag vermeldt de bestandscontrole, de taalreview en de controle in de game of winkelpreview afzonderlijk en geeft voor elk openstaand probleem de volgende stap. Keur termen in de projectwoordenlijst goed voordat je ze opnieuw gebruikt.

**Voorbeeldprompt voor een spreadsheet**

~~~text
Gebruik Game Localization om de kolom ENGLISH in de bijgevoegde werkmap naar het Duits (de-DE) te vertalen. Schrijf de vertalingen naar GERMAN in een nieuwe .xlsx-kopie. Gebruik de bijgevoegde woordenlijst en DESCRIPTION als context. Behoud sleutels, bronkolommen, tijdelijke aanduidingen en tags. Vermeld terminologievragen en controles afzonderlijk, met rij-ID’s.
~~~

**Voorbeeldprompt voor een winkelpagina**

~~~text
Gebruik Game Localization om deze korte Steam-beschrijving uit het Engels naar Braziliaans Portugees (pt-BR) te vertalen. Begin indien nodig een conceptwoordenlijst. Behoud de gametitel en houd je aan de opgegeven tekenlimiet. Geef de winkeltekst en een afzonderlijk overdrachtsverslag terug.
~~~

### CSV-vertalingen controleren

Geef voor een CSV-bestand met vaste rij-ID’s de kolomkoppen voor ID, brontekst en vertaling op. Als Python 3.9 of hoger beschikbaar is, vergelijkt de skill het bronbestand met het vertaalde bestand en meldt ontbrekende of dubbele ID’s, lege vertalingen, wijzigingen aan ondersteunde tijdelijke aanduidingen of tags en overschrijdingen van de lengtelimiet. [Instructies voor CSV-controle](../game-localization/references/csv-qa.md)

Probeer het [instapvoorbeeld met 12 rijen](../game-localization/examples/first-run/README.md). Het bevat een conceptvertaling, een goedgekeurde woordenlijst en een voorbeeld van het overdrachtsverslag.

### Onze modelinstellingen

| Omgeving | Model | Redeneerniveau |
| --- | --- | --- |
| ChatGPT Work of Codex | GPT-6.1 Sol | High of hoger, indien beschikbaar |
| Claude | Claude Opus 5.5 | High of hoger, indien beschikbaar |

**High+** staat voor High of hoger, afhankelijk van de opties in de client. Kies daar het model en niveau. De skill werkt onafhankelijk van deze voorkeur. [OpenAI-modelinstellingen](https://learn.chatgpt.com/docs/models) · [Redeneerniveaus van Claude](https://platform.claude.com/docs/en/build-with-claude/effort)

## Bijwerken of verwijderen

| Installatiemethode | Bijwerken | Verwijderen |
| --- | --- | --- |
| ChatGPT- of Codex-plug-in | Als je de upload beheert, kies je **Upload new version** in de details. Installaties uit een catalogus of werkruimte worden vanuit die bron bijgewerkt. | Open **Plugins → Installed → Game Localization** en kies **Uninstall plugin** indien beschikbaar. Vraag bij een beheerde installatie de beheerder. |
| Losse ChatGPT-skill | Vervang je persoonlijke upload door de nieuwste losse ZIP via het skillbeheer. | Zoek de skill in **Plugins → Skills** onder **Installed** of **Created by me** en gebruik de verwijderoptie. Beheerders beheren skills van de werkruimte. |
| Aangepaste Claude-skill | Upload de nieuwe losse ZIP via de beheerpagina. Schakel de oude versie uit als er een tweede item verschijnt. | Open de skill in **Customize → Skills** of **Plugins** en schakel die uit. Kies voor je eigen upload **⋯ → Delete** en bevestig. |
| Lokale skill via Skills CLI | Voer voor een gevolgde branch `npx skills update game-localization` uit of installeer vanuit de nieuwe tag. | Voer in hetzelfde project `npx skills remove game-localization` uit. Voeg `-g` toe bij een globale installatie. |
| Lokale map of Codex Skill Installer | Vervang de geïnstalleerde map `game-localization/` door de nieuwste versie. | Verwijder `game-localization/`. Codex laadt die uit `.agents/skills/`, `~/.agents/skills/` of `~/.codex/skills/`. Claude Code gebruikt `.claude/skills/` of `~/.claude/skills/`. Start zo nodig een nieuwe sessie. |

[OpenAI-plug-ins beheren](https://learn.chatgpt.com/docs/plugins) · [Aangepaste Claude-skills beheren](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Broncode en pakketten

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) bepaalt wanneer de skill start en hoe een tekstpakket wordt verwerkt.
- [`game-localization/references/`](../game-localization/references/) bevat de regels en woordenlijsten per taal.
- [`packaging/chatgpt/`](../packaging/chatgpt/) bevat het manifest en pictogram van de plug-in.
- [`packages/`](../packages/) bevat de uploadbare archieven.

Bouw beide ZIP’s opnieuw uit dezelfde bron met `python scripts/package.py` in de hoofdmap van de repository en Python 3.9 of hoger. De versie komt uit het ChatGPT-manifest. Upload vóór verspreiding elke ZIP naar het juiste product en test met een klein tekstpakket, woordenlijst en beschermde tijdelijke aanduiding.

## Licentie

Game Localization is beschikbaar onder de [MIT-licentie](../LICENSE). Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## De maker steunen

Als Game Localization je team helpt, kun je [Maled1kt steunen via DonationAlerts](https://www.donationalerts.com/r/maled1kt). Donaties zijn vrijwillig.
