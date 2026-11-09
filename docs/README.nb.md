# Game Localization

![Game Localization by Maled1kt](../assets/game-localization-banner.png)

[English](../README.md) · [Alle språk](../README.md#languages)

Game Localization er en agentferdighet for oversetting, redigering og kvalitetssikring av spilltekster i ChatGPT, Codex og Claude. Den dekker menyer, opplæring, dialog, undertekster, butikktekster og prosjektdokumentasjon for Steam, PlayStation, Xbox og mobilspill.

[Installasjon](#installasjon) · [Bruke ferdigheten](#bruke-ferdigheten) · [Oppdatere eller fjerne](#oppdatere-eller-fjerne) · [Støtt opphavspersonen](#støtt-opphavspersonen) · [Utviklingsplan](../ROADMAP.md) · [Endringslogg](../CHANGELOG.md)

## Funksjoner

- Bruker godkjent prosjektterminologi og registrerer nye termer som forslag.
- Bevarer lokaliseringsnøkler, plassholdere som `{player_name}` og `%s`, tagger, betydningsfulle linjeskift og andre beskyttede elementer.
- Kontrollerer oppgitte lengdegrenser og holder oversettelsen adskilt fra spørsmål, kildekorrigeringer og kvalitetsnotater.
- Tilbyr et [forhåndsvalg med 30 språk og varianter](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages) og støtter egne lister.
- Inneholder en [startordliste med 75 termer på alle 30 språk og varianter](../game-localization/references/glossary/README.md), med felles engelske definisjoner og oversettelsesforslag.

Ferdigheten inneholder instrukser og referansefiler. Den krever ingen prosjekt-API-nøkkel, kobling eller bakgrunnstjeneste. Filredigering avhenger av verktøyene i chatten. Før utgivelse, kontroller grensesnittet i spillbuilden og butikkteksten i plattformens forhåndsvisning.

## Installasjon

| Miljø | Pakke |
| --- | --- |
| ChatGPT eller Codex med tillatelse til å laste opp programtillegg | [ZIP for ChatGPT-programtillegget](../packages/game-localization-chatgpt-v0.1.8.zip) |
| Claude eller ChatGPT-arbeidsområder som kan laste opp frittstående ferdigheter | [ZIP for frittstående ferdighet](../packages/game-localization-skill-v0.1.8.zip) |
| Lokal Codex eller Claude Code | [Installer fra kildemappen](#installer-for-lokale-agenter-med-én-kommando) |

Åpne pakkelenken på GitHub og velg **Download raw file**. Last opp ZIP-filen uten å pakke den ut.

### ChatGPT og Codex

1. Åpne kontoens opplastingsvalg i ChatGPT på nett. Eiere og administratorer med tillatelse kan bruke **Admin console → Plugins → Add → Upload plugin**.
2. Velg ZIP-filen for programtillegget. Etter validering åpner du **Game Localization** i **Plugins** og velger **Install plugin** hvis tilgjengelig. Personlige opplastinger kan vises under **Personal → Created by me**.
3. Åpne en ny chat i ChatGPT eller Codex. Skriv `@` og velg **Game Localization** fra forslagene.

Hvis arbeidsområdet støtter frittstående ferdigheter, laster du opp ZIP-filen via **Plugins → Skills → Create → Upload from your computer**. Vent på skanningen og følg anvisningene. Valgene avhenger av konto og arbeidsområde. [OpenAI-veiledning for programtillegg](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [OpenAI-veiledning for ferdigheter](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. Slå på **Code execution and file creation** i Claude hvis kontoen eller arbeidsområdet krever det.
2. Åpne **Customize → Skills** i Claude på nett eller i Claude Desktop. I den nye visningen åpner du **Plugins** i sidefeltet og finner ferdighetskontrollene under **Your plugins**.
3. Velg **+ → Create skill → Upload a skill** og den frittstående ZIP-filen. Slå på `game-localization` når den vises.
4. Åpne en ny chat og be Claude bruke **Game Localization**. Velg ferdigheten under **+** eller **/** i skrivefeltet hvis den vises der.

I administrerte arbeidsområder må en administrator kanskje aktivere eller laste opp ferdigheter. [Claude-veiledning for ferdigheter](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Nytt Claude-sidefelt](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### Installer for lokale agenter med én kommando

Kommandoene bruker `main`-grenen i [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization). De fungerer når repositoriet og grenen er publisert. Relative ZIP-lenker fungerer også på andre grener, tagger og forker.

Velg `$skill-installer` i en lokal Codex-chat og send forespørselen nedenfor. Godkjenn nettverkstilgang ved behov og start en ny økt. [Codex-veiledning for ferdigheter](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

Tredjepartsverktøyet Skills CLI kan installere samme kildemappe for lokal Codex og Claude Code med én kommando. Kjør den fra målprosjektet med Node.js 22.20 eller nyere. Behold `-a` for agentene du trenger. Legg til `-g` for installasjon på brukernivå. [Skills CLI-referanse](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

Bruk shellfeltet i den lokale Claude Code-terminalchatten for å installere bare for Claude. Sjekk repositoriets URL før du kjører kommandoen. [Shellfelt i Claude Code](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

Start en ny økt og bruk `$game-localization` i Codex eller `/game-localization` i Claude Code. For manuell installasjon kopierer du hele `game-localization/` til prosjektets `.claude/skills/` eller brukerens `~/.claude/skills/`. [Claude Code-veiledning for ferdigheter](https://code.claude.com/docs/en/skills)

Bruk kontoens opplastings- eller installasjonsvalg i nettversjonene av ChatGPT og Claude. En omtale i chatten aktiverer en installert ferdighet. For en delbar lenke kan du publisere via plattformens katalog eller dele ferdigheten eller programtillegget i et kvalifisert arbeidsområde. [Del ChatGPT-programtillegg](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Del Claude-ferdigheter](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Bruke ferdigheten

1. Legg ved kildeteksten eller filen og gjeldende prosjektordliste for målspråkene. Hvis det ikke finnes en ordliste, ber du uttrykkelig om et utkast.
2. Oppgi kilde- og målspråk, plattform, materialtype og utdataformat. Ta med tegngrenser, skjermbilder, talerinformasjon eller variabeleksempler når det er relevant.
3. For regneark oppgir du kilde- og målkolonner og ber om en ny kopi. For spilltekster oppgir du stabile ID-er eller nøkler. For butikktekst oppgir du målfelt og en eventuell streng lengdegrense.
4. Les de separate leveringsnotatene for å se om resultatet er klart til bruk eller fortsatt er et utkast. Notatene viser filkontroll, språklig gjennomgang og kontroll i spillet eller butikkens forhåndsvisning hver for seg og angir neste steg for hvert uavklarte problem. Godkjenn termer i prosjektordlisten før du gjenbruker dem.

Bruk [malen for prosjektordlisten](../game-localization/references/project-glossary-template.md) til å holde godkjente termer atskilt fra forslag. Lagre den oppdaterte filen og legg den ved i neste chat.

**Eksempel på ledetekst for regneark**

~~~text
Bruk Game Localization til å oversette ENGLISH-kolonnen i den vedlagte arbeidsboken til tysk (de-DE). Skriv oversettelsene i GERMAN i en ny .xlsx-kopi. Bruk den vedlagte ordlisten og DESCRIPTION som kontekst. Bevar nøkler, kildekolonner, plassholdere og tagger. Oppgi terminologispørsmål og kontroller separat med rad-ID-er.
~~~

For støttede `.xlsx`-filer oppgir du arket, overskriftsraden, kolonnen med faste rad-ID-er, kildekolonnen og den eksisterende målkolonnen. Med Python 3.9 eller nyere skriver ferdigheten oversettelsene etter ID i en ny kopi og kontrollerer at resten av arbeidsboken er bevart. Hvis arbeidsboken ikke kan kontrolleres, kan ferdigheten tilby en CSV-fil med ID-er. [Excel-veiledning](../game-localization/references/xlsx-qa.md)

**Eksempel på ledetekst for butikkside**

~~~text
Bruk Game Localization til å lokalisere denne korte Steam-beskrivelsen fra engelsk til brasiliansk portugisisk (pt-BR). Start et ordlisteutkast ved behov. Behold spilltittelen og overhold tegngrensen. Returner butikkteksten og separate leveringsnotater.
~~~

### Kontrollere CSV-oversettelser

For en CSV-fil med faste rad-ID-er oppgir du kolonneoverskriftene for ID, kildetekst og oversettelse. Hvis Python 3.9 eller nyere er tilgjengelig, sammenligner ferdigheten kildefilen med den oversatte filen og melder fra om manglende eller dupliserte ID-er, tomme oversettelser, endringer i støttede plassholdere eller tagger og overskredne lengdegrenser. [Veiledning for CSV-kontroll](../game-localization/references/csv-qa.md)

Prøv [starteksempelet med 12 rader](../game-localization/examples/first-run/README.md). Det inneholder et oversettelsesutkast, en godkjent ordliste og et eksempel på leveringsnotater.

### Våre modellinnstillinger

| Miljø | Modell | Resonneringsnivå |
| --- | --- | --- |
| ChatGPT Work eller Codex | GPT-6.1 Sol | High eller høyere, hvis tilgjengelig |
| Claude | Claude Opus 5.5 | High eller høyere, hvis tilgjengelig |

**High+** betyr High eller et høyere nivå som klienten tilbyr. Velg modell og nivå i klienten. Ferdigheten fungerer uavhengig av dette valget. [OpenAI-modellinnstillinger](https://learn.chatgpt.com/docs/models) · [Claudes resonneringsnivåer](https://platform.claude.com/docs/en/build-with-claude/effort)

## Oppdatere eller fjerne

| Installasjonsmåte | Oppdater | Fjern |
| --- | --- | --- |
| ChatGPT- eller Codex-programtillegg | Hvis du styrer opplastingen, velger du **Upload new version** i detaljene. Installasjoner fra en katalog eller et arbeidsområde oppdateres derfra. | Åpne **Plugins → Installed → Game Localization** og velg **Uninstall plugin** hvis tilgjengelig. Kontakt administratoren for administrerte installasjoner. |
| Frittstående ChatGPT-ferdighet | Erstatt den personlige opplastingen med nyeste frittstående ZIP via ferdighetsadministrasjonen. | Åpne **Plugins → Skills**, finn ferdigheten i **Installed** eller **Created by me**, og bruk fjerningsvalget hvis det finnes. Administratorer styrer arbeidsområdets ferdigheter. |
| Tilpasset Claude-ferdighet | Last opp den nye frittstående ZIP-filen fra administrasjonssiden. Deaktiver den gamle versjonen hvis du får en ekstra oppføring. | Åpne ferdigheten i **Customize → Skills** eller **Plugins** og slå den av. For en egen opplasting velger du **⋯ → Delete** og bekrefter. |
| Lokal ferdighet via Skills CLI | Kjør `npx skills update game-localization` for en fulgt gren, eller installer fra den nye taggen. | Kjør `npx skills remove game-localization` i samme prosjekt. Legg til `-g` ved global installasjon. |
| Lokal mappe eller Codex Skill Installer | Bytt ut den installerte `game-localization/`-mappen med nyeste versjon. | Fjern `game-localization/`. Codex kan laste den fra `.agents/skills/`, `~/.agents/skills/` eller `~/.codex/skills/`. Claude Code bruker `.claude/skills/` eller `~/.claude/skills/`. Start om nødvendig en ny økt. |

[Administrer OpenAI-programtillegg](https://learn.chatgpt.com/docs/plugins) · [Administrer tilpassede Claude-ferdigheter](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Kildekode og pakker

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) angir når ferdigheten brukes og hvordan den behandler en tekstgruppe.
- [`game-localization/references/`](../game-localization/references/) inneholder reglene og startordlistene for hvert språk.
- [`packaging/chatgpt/`](../packaging/chatgpt/) inneholder manifestet og ikonet for programtillegget.
- [`packages/`](../packages/) inneholder arkivene som kan lastes opp.

Bygg begge ZIP-filene på nytt fra samme kilde med `python scripts/package.py` i repositoriets rotmappe og Python 3.9 eller nyere. Versjonen hentes fra ChatGPT-manifestet. Last opp hver ZIP i riktig produkt før distribusjon, og prøv en liten tekstgruppe med ordliste og beskyttet plassholder.

## Lisens

Game Localization er tilgjengelig under [MIT-lisensen](../LICENSE). Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## Støtt opphavspersonen

Hvis Game Localization hjelper teamet ditt, kan du [støtte Maled1kt via DonationAlerts](https://www.donationalerts.com/r/maled1kt). Bidrag er helt frivillige.
