# Game Localization

![Game Localization-banner med to spildialogfelter, der udveksler tegn fra forskellige sprog](../assets/game-localization-banner.png)

[English](../README.md) · [Alle sprog](../README.md#languages)

Game Localization er en agentfærdighed til oversættelse, redigering og gennemgang af spiltekster i ChatGPT, Codex og Claude. Den omfatter menuer, vejledninger, dialog, undertekster, butikstekster og projektdokumentation til Steam, PlayStation, Xbox og mobilspil.

[Installation](#installation) · [Brug færdigheden](#brug-færdigheden) · [Opdater eller fjern](#opdater-eller-fjern) · [Støt ophavspersonen](#støt-ophavspersonen) · [Udviklingsplan](../ROADMAP.md) · [Ændringslog](../CHANGELOG.md)

## Funktioner

- Anvender godkendt projektterminologi og registrerer nye termer som forslag.
- Bevarer lokaliseringsnøgler, pladsholdere som `{player_name}` og `%s`, tags, betydningsfulde linjeskift og andre beskyttede elementer.
- Kontrollerer angivne længdegrænser og adskiller oversættelsen fra spørgsmål, rettelser af kildeteksten og kvalitetsnoter.
- Tilbyder en [standardliste med 30 sprog og varianter](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages) og understøtter brugerdefinerede lister.
- Indeholder en [startordliste med 75 termer på alle 30 sprog og varianter](../game-localization/references/glossary/README.md), med fælles engelske definitioner og oversættelsesforslag.

Færdigheden indeholder instruktioner og referencefiler. Den kræver ingen projekt-API-nøgle, connector eller baggrundstjeneste. Filredigering afhænger af værktøjerne i chatten. Kontrollér før udgivelse den oversatte brugerflade i spilbuildet og butiksteksten i platformens forhåndsvisning.

## Installation

| Miljø | Pakke |
| --- | --- |
| ChatGPT eller Codex med tilladelse til at uploade plugins | [ZIP til ChatGPT-plugin](../packages/game-localization-chatgpt-v0.1.6.zip) |
| Claude eller ChatGPT-arbejdsområder, der må uploade selvstændige færdigheder | [ZIP til selvstændig færdighed](../packages/game-localization-skill-v0.1.6.zip) |
| Lokal Codex eller Claude Code | [Installér fra kildemappen](#installation-af-lokale-agenter-med-én-kommando) |

Åbn pakkelinket på GitHub, og vælg **Download raw file**. Upload ZIP-filen uden at pakke den ud.

### ChatGPT og Codex

1. Åbn kontoens plugin-upload i ChatGPT på nettet. Ejere og administratorer med tilladelse kan bruge **Admin console → Plugins → Add → Upload plugin**.
2. Vælg pluginets ZIP-fil. Efter valideringen åbner du **Game Localization** under **Plugins** og vælger **Install plugin**, hvis det vises. Personlige uploads kan ligge under **Personal → Created by me**.
3. Åbn en ny chat i ChatGPT eller Codex. Skriv `@`, og vælg **Game Localization** blandt forslagene.

Hvis arbejdsområdet understøtter selvstændige færdigheder, kan du uploade ZIP-filen via **Plugins → Skills → Create → Upload from your computer**. Vent på scanningen, og følg anvisningerne. Mulighederne afhænger af konto og arbejdsområde. [OpenAI-vejledning til plugins](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [OpenAI-vejledning til færdigheder](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. Slå **Code execution and file creation** til i Claude, hvis kontoen eller arbejdsområdet kræver det.
2. Åbn **Customize → Skills** i Claude på nettet eller i Claude Desktop. I det nye layout åbner du **Plugins** i sidepanelet og finder styringen under **Your plugins**.
3. Vælg **+ → Create skill → Upload a skill**, og vælg den selvstændige ZIP-fil. Aktivér `game-localization`, når den vises.
4. Åbn en ny chat, og bed Claude bruge **Game Localization**. Vælg færdigheden under **+** eller **/** i skrivefeltet, hvis den vises der.

I administrerede arbejdsområder skal en administrator muligvis aktivere eller uploade færdigheder. [Claude-vejledning til færdigheder](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Ny Claude-sidebjælke](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### Installation af lokale agenter med én kommando

Kommandoerne bruger grenen `main` fra [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization). De virker, når repositoriet og grenen er offentliggjort. De relative ZIP-links virker også på andre grene, tags og forks.

I en lokal Codex-chat vælger du `$skill-installer` og sender anmodningen nedenfor. Tillad om nødvendigt netværksadgang, og start en ny session. [Codex-vejledning til færdigheder](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

Tredjepartsværktøjet Skills CLI kan installere samme kildemappe til lokal Codex og Claude Code med én kommando. Kør den i det ønskede projekt med Node.js 22.20 eller nyere. Behold `-a` for de agenter, du vil bruge. Tilføj `-g` for installation på brugerniveau. [Skills CLI-reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

I den lokale Claude Code-terminalchat kan du installere kun til Claude via shellinput. Kontrollér repositoriets URL, før du kører kommandoen. [Shellinput i Claude Code](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

Kald `$game-localization` i Codex eller `/game-localization` i Claude Code i en ny session. Ved manuel installation kopierer du hele mappen `game-localization/` til `.claude/skills/` i projektet eller til brugerens `~/.claude/skills/`. [Claude Code-vejledning til færdigheder](https://code.claude.com/docs/en/skills)

I de hostede udgaver af ChatGPT og Claude bruger du kontoens upload- eller installationsfunktion. En omtale i chatten aktiverer en installeret færdighed. For at få et installationslink, der kan deles, kan du udgive via platformens katalog eller dele færdigheden eller pluginet i et arbejdsområde med adgang. [Deling af ChatGPT-plugins](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Deling af Claude-færdigheder](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Brug færdigheden

1. Vedhæft kildeteksten eller -filen og den aktuelle projektordliste for målsprogene. Hvis der ikke findes en ordliste, skal du udtrykkeligt bede om et udkast.
2. Angiv kilde- og målsprog, platform, materialetype og outputformat. Medtag efter behov tegngrænser, skærmbilleder, oplysninger om talere eller eksempler på variabler.
3. Ved regneark skal du navngive kilde- og målkolonner og bede om en ny kopi. Ved spiltekster skal du angive stabile ID’er eller nøgler. Ved butikstekst skal du angive felt og en eventuel fast længdegrænse.
4. Læs de separate afleveringsnoter for at se, om resultatet er klar til brug eller stadig er et udkast. Noterne viser filkontrol, sproglig gennemgang og kontrol i spillet eller butikkens forhåndsvisning hver for sig og angiver næste skridt for hvert åbent problem. Godkend termerne i projektordlisten, før du genbruger dem.

**Eksempel på prompt til regneark**

~~~text
Brug Game Localization til at oversætte kolonnen ENGLISH i den vedhæftede projektmappe til tysk (de-DE). Skriv oversættelserne i GERMAN i en ny .xlsx-kopi. Brug den vedhæftede ordliste og kolonnen DESCRIPTION som kontekst. Bevar nøgler, kildekolonner, pladsholdere og tags. Angiv terminologispørgsmål og kontroller separat med række-ID’er.
~~~

**Eksempel på prompt til butiksside**

~~~text
Brug Game Localization til at lokalisere denne korte Steam-beskrivelse fra engelsk til brasiliansk portugisisk (pt-BR). Start et udkast til en ordliste, hvis det er nødvendigt. Bevar spillets titel, og overhold tegngrænsen. Returnér butiksteksten og separate afleveringsnoter.
~~~

### Kontrol af CSV-oversættelser

For en CSV-fil med faste række-id’er skal du angive kolonneoverskrifterne for id, kildetekst og oversættelse. Hvis Python 3.9 eller nyere er tilgængelig, sammenligner færdigheden kildefilen med den oversatte fil og markerer manglende eller dublerede id’er, tomme oversættelser, ændringer i understøttede pladsholdere eller tags samt overskredne længdegrænser. [Vejledning til CSV-kontrol](../game-localization/references/csv-qa.md)

Prøv [starteksemplet med 12 rækker](../game-localization/examples/first-run/README.md). Det indeholder et oversættelsesudkast, en godkendt ordliste og et eksempel på afleveringsnoter.

### Vores modelindstillinger

| Miljø | Model | Ræsonneringsniveau |
| --- | --- | --- |
| ChatGPT Work eller Codex | GPT-6.1 Sol | High eller højere, hvis det er tilgængeligt |
| Claude | Claude Opus 5.5 | High eller højere, hvis det er tilgængeligt |

**High+** betyder High eller et højere niveau i klienten. Vælg model og niveau i klienten. Færdigheden virker uafhængigt af indstillingen. [OpenAI-modelindstillinger](https://learn.chatgpt.com/docs/models) · [Claudes ræsonneringsniveauer](https://platform.claude.com/docs/en/build-with-claude/effort)

## Opdater eller fjern

| Installationsmetode | Opdater | Fjern |
| --- | --- | --- |
| Plugin til ChatGPT eller Codex | Hvis du administrerer uploadet, vælger du **Upload new version** i pluginets detaljer. Installationer fra et katalog eller arbejdsområde får opdateringer derfra. | Åbn **Plugins → Installed → Game Localization**, og vælg **Uninstall plugin**, hvis den er tilgængelig. Spørg administratoren ved en administreret installation. |
| Selvstændig ChatGPT-færdighed | Erstat dit personlige upload med den nyeste selvstændige ZIP via færdighedsstyringen. | Åbn **Plugins → Skills**, find færdigheden under **Installed** eller **Created by me**, og brug fjernelsesfunktionen, hvis den er tilgængelig. Administratorerne styrer arbejdsområdets færdigheder. |
| Tilpasset Claude-færdighed | Upload den nye selvstændige ZIP via styringssiden. Deaktivér den gamle version, hvis der oprettes en ekstra post. | Åbn i **Customize → Skills** eller **Plugins**, og deaktivér færdigheden. For dit eget upload vælger du **⋯ → Delete** og bekræfter. |
| Lokal færdighed via Skills CLI | Kør `npx skills update game-localization` for en fulgt gren, eller installér fra det nye tag. | Kør `npx skills remove game-localization` i samme projekt. Tilføj `-g` ved global installation. |
| Lokal mappe eller Codex Skill Installer | Erstat den installerede mappe `game-localization/` med den nyeste version. | Fjern `game-localization/`. Codex kan indlæse den fra `.agents/skills/`, `~/.agents/skills/` eller `~/.codex/skills/`. Claude Code bruger `.claude/skills/` eller `~/.claude/skills/`. Start om nødvendigt en ny session. |

[Administration af OpenAI-plugins](https://learn.chatgpt.com/docs/plugins) · [Administration af tilpassede Claude-færdigheder](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Kildekode og pakker

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) fastlægger, hvornår færdigheden aktiveres, og hvordan den behandler en portion tekster.
- [`game-localization/references/`](../game-localization/references/) indeholder reglerne og startordlisterne for hvert sprog.
- [`packaging/chatgpt/`](../packaging/chatgpt/) indeholder pluginets manifest og ikon.
- [`packages/`](../packages/) indeholder arkiver til upload.

Gendan begge ZIP-filer fra samme kilde med `python scripts/package.py` i repositoriets rod med Python 3.9 eller nyere. Versionen stammer fra ChatGPT-pluginets manifest. Upload hvert arkiv i det relevante produkt før distribution, og test et lille sæt tekster med ordliste og beskyttet pladsholder.

## Licens

Game Localization er tilgængelig under [MIT-licensen](../LICENSE). Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## Støt ophavspersonen

Hvis Game Localization hjælper dit team, kan du [støtte Maled1kt via DonationAlerts](https://www.donationalerts.com/r/maled1kt). Donationer er helt frivillige.
