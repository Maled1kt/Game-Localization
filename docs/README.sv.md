# Game Localization

![Game Localization by Maled1kt](../assets/game-localization-banner.png)

[English](../README.md) · [Alla språk](../README.md#languages)

Game Localization är en agentfärdighet för att översätta, redigera och granska speltexter i ChatGPT, Codex och Claude. Den omfattar menyer, handledningar, dialog, undertexter, butikstexter och projektdokumentation för Steam, PlayStation, Xbox och mobilspel.

[Installation](#installation) · [Använd färdigheten](#använd-färdigheten) · [Uppdatera eller ta bort](#uppdatera-eller-ta-bort) · [Stöd upphovspersonen](#stöd-upphovspersonen) · [Utvecklingsplan](../ROADMAP.md) · [Ändringslogg](../CHANGELOG.md)

## Funktioner

- Använder godkänd projektterminologi och registrerar nya termer som förslag.
- Bevarar lokaliseringsnycklar, platshållare som `{player_name}` och `%s`, taggar, betydelsebärande radbrytningar och andra skyddade element.
- Kontrollerar angivna längdgränser och håller översättningen åtskild från frågor, källrättelser och anteckningar om kvalitetskontroll.
- Erbjuder en [förinställd lista med 30 språk och varianter](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages) och stöder egna listor.
- Innehåller en [startordlista med 75 termer på alla 30 språk och varianter](../game-localization/references/glossary/README.md), med gemensamma engelska definitioner och översättningsförslag.

Färdigheten innehåller instruktioner och referensfiler. Den kräver ingen projekt-API-nyckel, anslutning eller bakgrundstjänst. Filredigering beror på verktygen i chatten. Granska det översatta gränssnittet i spelbygget och butikstexten i plattformens förhandsvisning före publicering.

## Installation

| Miljö | Paket |
| --- | --- |
| ChatGPT eller Codex med behörighet att ladda upp tillägg | [ZIP för ChatGPT-tillägget](../packages/game-localization-chatgpt-v0.1.12.zip) |
| Claude eller ChatGPT-arbetsytor som får ladda upp fristående färdigheter | [ZIP för fristående färdighet](../packages/game-localization-skill-v0.1.12.zip) |
| Lokal Codex eller Claude Code | [Installera från källmappen](#installera-för-lokala-agenter-med-ett-kommando) |

I lokal Codex och Claude Code kan du installera Game Localization från den gemensamma GitHub-katalogen. Guiden beskriver den första installationen, bytet från ZIP och hur varje klient uppdateras. [GitHub-katalog](plugin-catalog.md)

Öppna paketlänken på GitHub och välj **Download raw file**. Ladda upp ZIP-filen utan att packa upp den.

### ChatGPT och Codex

1. Öppna kontots uppladdning av tillägg i ChatGPT på webben. Behöriga ägare och administratörer kan använda **Admin console → Plugins → Add → Upload plugin**.
2. Välj tilläggets ZIP. Efter valideringen öppnar du **Game Localization** i **Plugins** och väljer **Install plugin** om det finns. Personliga uppladdningar kan visas i **Personal → Created by me**.
3. Öppna en ny chatt i ChatGPT eller Codex. Skriv `@` och välj **Game Localization** bland förslagen.

Om arbetsytan stöder fristående färdigheter laddar du upp motsvarande ZIP via **Plugins → Skills → Create → Upload from your computer**. Vänta på genomsökningen och följ anvisningarna. Alternativen beror på konto och arbetsyta. [OpenAI-guide för tillägg](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [OpenAI-guide för färdigheter](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. Aktivera **Code execution and file creation** i Claude om kontot eller arbetsytan kräver det.
2. Öppna **Customize → Skills** i Claude på webben eller i Claude Desktop. I den nya layouten öppnar du **Plugins** i sidofältet och hittar hanteringen under **Your plugins**.
3. Välj **+ → Create skill → Upload a skill** och den fristående ZIP-filen. Aktivera `game-localization` när den visas.
4. Öppna en ny chatt och be Claude använda **Game Localization**. Välj färdigheten under **+** eller **/** i inmatningsfältet om den visas där.

På en hanterad arbetsyta kan en administratör behöva aktivera eller ladda upp färdigheter. [Claude-guide för färdigheter](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Nytt sidofält i Claude](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### Installera för lokala agenter med ett kommando

Kommandona använder grenen `main` i [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization). De fungerar när kodförrådet och grenen har publicerats. De relativa ZIP-länkarna fungerar även på andra grenar, taggar och förgreningar.

Välj `$skill-installer` i en lokal Codex-chatt och skicka begäran nedan. Godkänn nätverksåtkomst om det efterfrågas och starta en ny session. [Codex-guide för färdigheter](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

Tredjepartsverktyget Skills CLI kan installera samma källmapp för lokal Codex och Claude Code med ett kommando. Kör det i målprojektet med Node.js 22.20 eller senare. Behåll `-a` för de agenter du behöver. Lägg till `-g` för installation på användarnivå. [Referens för Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

Använd skalinmatningen i den lokala terminalchatten i Claude Code för att installera endast för Claude. Kontrollera kodförrådets URL innan du kör kommandot. [Skalinmatning i Claude Code](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

Anropa `$game-localization` i Codex eller `/game-localization` i Claude Code i en ny session. Vid manuell installation kopierar du hela `game-localization/` till projektets `.claude/skills/` eller användarens `~/.claude/skills/`. [Claude Code-guide för färdigheter](https://code.claude.com/docs/en/skills)

Använd kontots uppladdnings- eller installationsalternativ i de värdbaserade versionerna av ChatGPT och Claude. Ett omnämnande anropar den installerade färdigheten. För en delbar länk kan du publicera via plattformens katalog eller dela färdigheten eller tillägget i en behörig arbetsyta. [Dela ChatGPT-tillägg](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Dela Claude-färdigheter](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Använd färdigheten

1. Bifoga källtexten eller filen och projektets aktuella ordlista för målspråken. Be uttryckligen om ett utkast om ordlista saknas.
2. Ange käll- och målspråk, plattform, materialtyp och utdataformat. Lägg vid behov till teckengränser, skärmbilder, information om talare eller exempelvärden för variabler.
3. För kalkylblad anger du käll- och målkolumnerna och ber om en ny kopia. För speltexter ger du stabila ID:n eller nycklar. För butikstexter anger du målfältet och en eventuell strikt längdgräns.
4. Läs de separata leveransanteckningarna för att se om resultatet är klart att använda eller fortfarande är ett utkast. Anteckningarna redovisar filkontroll, språkgranskning och kontroll i spelet eller butikens förhandsvisning var för sig. De visar också nästa steg för varje olöst problem. Godkänn termerna i projektordlistan innan du återanvänder dem.

För spelets gränssnitt innehåller överlämningen en prioriterad checklista med skärm, sträng-ID, steg för att återskapa fallet och godkännandekriterier. Långa infogade värden och text som kan klippas av kontrolleras först. Om teckensnittet och den tillgängliga bredden är kända kan färdigheten uppskatta platsbehovet. [Kontroller i spelet](../game-localization/references/in-build-qa.md)

Använd [mallen för projektordlistan](../game-localization/references/project-glossary-template.md) för att hålla godkända termer åtskilda från förslag. Spara den uppdaterade filen och bifoga den i nästa chatt.

**Exempel på uppmaning för kalkylblad**

~~~text
Använd Game Localization för att översätta kolumnen ENGLISH i den bifogade arbetsboken till tyska (de-DE). Skriv översättningen i GERMAN i en ny .xlsx-kopia. Använd ordlistan och kolumnen DESCRIPTION som kontext. Bevara nycklar, källkolumner, platshållare och taggar. Lista termfrågor och kontroller separat med rad-ID:n.
~~~

För `.xlsx`-filer som stöds anger du blad, rubrikrad, kolumn med stabila rad-ID:n, källkolumn och befintlig målkolumn. Med Python 3.9 eller senare skriver färdigheten översättningarna efter ID i en ny kopia och kontrollerar att resten av arbetsboken har bevarats. Om arbetsboken inte kan kontrolleras kan färdigheten erbjuda en CSV-fil med ID:n. [Excel-instruktioner](../game-localization/references/xlsx-qa.md)

**Exempel på uppmaning för butikssida**

~~~text
Använd Game Localization för att lokalisera den här korta Steam-beskrivningen från engelska till brasiliansk portugisiska (pt-BR). Börja vid behov på ett ordlisteutkast. Bevara speltiteln och följ angiven teckengräns. Lämna butikstexten och separata leveransanteckningar.
~~~

För Steam-sidor levererar färdigheten den korta beskrivningen och avsnittet Om detta spel var för sig, kontrollerar angivna gränser och påståenden om spelet och kan förbereda ett utkast från en Steamworks-JSON-export som stöds. I överlämningen följs import och förhandsvisning upp separat. [Arbetsflöde för Steam-sidor](../game-localization/references/steam-store.md)

### Kontrollera CSV-översättningar

För en CSV-fil med fasta rad-ID:n anger du kolumnrubrikerna för ID, källtext och översättning. Om Python 3.9 eller senare är tillgängligt jämför färdigheten källfilen med den översatta filen och rapporterar saknade eller dubbla ID:n, tomma översättningar, ändringar i platshållare eller taggar som stöds samt överskridna längdgränser. [Instruktioner för CSV-kontroll](../game-localization/references/csv-qa.md)

Bifoga föregående och aktuell käll-CSV, godkända översättningar och eventuella senare redaktörsändringar när du uppdaterar en översättning. Färdigheten matchar rader efter ID, behåller användbara översättningar för oförändrade rader och markerar tillagda, ändrade och borttagna rader. Spara läget efter varje scen i långa dialoger så att du kan fortsätta med samma arbetsfil. [Uppdatera CSV-översättningar](../game-localization/references/csv-updates.md)

Prova [startexemplet med 12 rader](../game-localization/examples/first-run/README.md). Det innehåller ett översättningsutkast, en godkänd ordlista och ett exempel på leveransanteckningar.

### Våra modellinställningar

| Miljö | Modell | Resonemangsnivå |
| --- | --- | --- |
| ChatGPT Work eller Codex | GPT-6.1 Sol | High eller högre, om tillgängligt |
| Claude | Claude Opus 5.5 | High eller högre, om tillgängligt |

**High+** betyder High eller en högre nivå i klienten. Välj modell och nivå i klienten. Färdigheten fungerar oberoende av det här valet. [OpenAI-modellinställningar](https://learn.chatgpt.com/docs/models) · [Claudes resonemangsnivåer](https://platform.claude.com/docs/en/build-with-claude/effort)

## Uppdatera eller ta bort

| Installationssätt | Uppdatera | Ta bort |
| --- | --- | --- |
| ChatGPT- eller Codex-tillägg | Om du hanterar uppladdningen väljer du **Upload new version** i tilläggets detaljer. Installationer från en katalog eller arbetsyta uppdateras från den källan. | Öppna **Plugins → Installed → Game Localization** och välj **Uninstall plugin** om det finns. Fråga administratören om en hanterad installation. |
| Fristående ChatGPT-färdighet | Byt ut din personliga uppladdning mot senaste fristående ZIP via hanteringen av färdigheter. | Öppna **Plugins → Skills**, leta under **Installed** eller **Created by me** och använd borttagningsfunktionen om den finns. Administratörer hanterar arbetsytans färdigheter. |
| Anpassad Claude-färdighet | Ladda upp den nya fristående ZIP-filen från hanteringssidan. Inaktivera den tidigare versionen om en andra post skapas. | Öppna färdigheten i **Customize → Skills** eller **Plugins** och stäng av den. Välj **⋯ → Delete** för din egen uppladdning och bekräfta. |
| Lokal färdighet via Skills CLI | Kör `npx skills update game-localization` för en följd gren eller installera från den nya taggen. | Kör `npx skills remove game-localization` i samma projekt. Lägg till `-g` vid global installation. |
| Lokal mapp eller Codex Skill Installer | Byt ut den installerade mappen `game-localization/` mot senaste versionen. | Ta bort `game-localization/`. Codex kan läsa från `.agents/skills/`, `~/.agents/skills/` eller `~/.codex/skills/`. Claude Code använder `.claude/skills/` eller `~/.claude/skills/`. Starta en ny session vid behov. |

[Hantera OpenAI-tillägg](https://learn.chatgpt.com/docs/plugins) · [Hantera anpassade Claude-färdigheter](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Källkod och paketering

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) anger när färdigheten körs och hur den hanterar ett textpaket.
- [`game-localization/references/`](../game-localization/references/) innehåller reglerna och språkversionerna av startordlistan.
- [`packaging/chatgpt/`](../packaging/chatgpt/) innehåller tilläggets manifest och ikon.
- [`packages/`](../packages/) innehåller arkiven för uppladdning.

Bygg båda ZIP-filerna från samma källa med `python scripts/package.py` i kodförrådets rot och Python 3.9 eller senare. Versionen kommer från ChatGPT-tilläggets manifest. Ladda upp varje ZIP till rätt produkt före distribution och testa ett litet textpaket med ordlista och skyddad platshållare.

## Licens

Game Localization är tillgängligt under [MIT-licensen](../LICENSE). Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## Stöd upphovspersonen

Om Game Localization hjälper ditt team kan du [stödja Maled1kt via DonationAlerts](https://www.donationalerts.com/r/maled1kt). Bidrag är helt frivilliga.
