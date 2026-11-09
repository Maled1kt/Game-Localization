# Game Localization

![Game Localization by Maled1kt](../assets/game-localization-banner.png)

[English](../README.md) · [Všechny jazyky](../README.md#languages)

Game Localization je dovednost pro agenty, která překládá, upravuje a kontroluje herní texty v ChatGPT, Codex a Claude. Hodí se pro nabídky, výukové texty, dialogy, titulky, texty obchodů a projektovou dokumentaci pro Steam, PlayStation, Xbox a mobilní hry.

[Instalace](#instalace) · [Používání dovednosti](#používání-dovednosti) · [Aktualizace a odstranění](#aktualizace-a-odstranění) · [Podpora autora](#podpora-autora) · [Plán vývoje](../ROADMAP.md) · [Přehled změn](../CHANGELOG.md)

## Funkce

- Používá schválenou terminologii projektu a zaznamenává nové termíny jako návrhy.
- Zachovává lokalizační klíče, zástupné symboly jako `{player_name}` a `%s`, značky, významové konce řádků a další chráněné prvky.
- Kontroluje limity délky a odděluje překlady od dotazů, oprav zdroje a poznámek z kontroly kvality.
- Nabízí [výchozí seznam 30 jazyků a variant](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages) a umožňuje zadat vlastní.
- Obsahuje [výchozí glosář 75 termínů ve všech 30 jazycích a variantách](../game-localization/references/glossary/README.md) se společnými anglickými definicemi a návrhy překladů.

Dovednost obsahuje pokyny a referenční soubory. Funguje bez projektového klíče API, konektoru či služby na pozadí. Úpravy souborů závisí na nástrojích dostupných v chatu. Před vydáním zkontrolujte rozhraní v sestavení hry a texty obchodu v náhledu platformy.

## Instalace

| Prostředí | Balíček |
| --- | --- |
| ChatGPT nebo Codex s oprávněním nahrávat pluginy | [ZIP pluginu ChatGPT](../packages/game-localization-chatgpt-v0.1.9.zip) |
| Claude nebo pracovní prostory ChatGPT s možností nahrát samostatnou dovednost | [ZIP samostatné dovednosti](../packages/game-localization-skill-v0.1.9.zip) |
| Místní Codex nebo Claude Code | [Instalace ze složky se zdroji](#instalace-pro-místní-agenty-jedním-příkazem) |

Otevřete odkaz na GitHubu a zvolte **Download raw file**. Nahrajte nerozbalený ZIP.

### ChatGPT a Codex

1. Ve webovém ChatGPT otevřete možnost nahrávání pluginů. Vlastníci a správci s příslušným oprávněním mohou použít **Admin console → Plugins → Add → Upload plugin**.
2. Vyberte ZIP pluginu. Po ověření otevřete **Game Localization** v **Plugins** a vyberte **Install plugin**, pokud se nabízí. Osobní nahrávka se může zobrazit v **Personal → Created by me**.
3. Otevřete nový chat v ChatGPT nebo Codex. Zadejte `@` a vyberte **Game Localization** z nabídky.

Pokud pracovní prostor podporuje samostatné dovednosti, nahrajte jejich ZIP přes **Plugins → Skills → Create → Upload from your computer**. Počkejte na kontrolu a postupujte podle pokynů. Dostupnost závisí na účtu a pracovním prostoru. [Příručka pluginů OpenAI](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Příručka dovedností OpenAI](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. Zapněte **Code execution and file creation** v nastavení Claude, pokud to účet nebo pracovní prostor vyžaduje.
2. Ve webovém Claude nebo Claude Desktop otevřete **Customize → Skills**. V novém rozhraní otevřete **Plugins** na postranním panelu a vyhledejte správu v **Your plugins**.
3. Vyberte **+ → Create skill → Upload a skill** a ZIP samostatné dovednosti. Aktivujte `game-localization`, jakmile se objeví.
4. Otevřete nový chat a požádejte Claude, aby použil **Game Localization**. Pokud se dovednost zobrazuje pod **+** nebo **/** v poli zprávy, vyberte ji tam.

Ve spravovaném pracovním prostoru může dovednosti povolovat nebo nahrávat správce. [Příručka dovedností Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Nový postranní panel Claude](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### Instalace pro místní agenty jedním příkazem

Příkazy používají větev `main` repozitáře [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization). Fungují po zveřejnění repozitáře i větve. Relativní odkazy na ZIP fungují také v jiných větvích, značkách a odvozených repozitářích.

V místním chatu Codex vyberte vestavěný `$skill-installer` a odešlete následující požadavek. Je-li to potřeba, povolte síť a zahajte novou relaci. [Příručka dovedností Codex](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

Nástroj třetí strany Skills CLI nainstaluje tutéž zdrojovou složku pro místní Codex a Claude Code jedním příkazem. Spusťte ho z cílového projektu s Node.js 22.20 nebo novějším. Ponechte volby `-a` pro potřebné agenty. Přidejte `-g` pro instalaci na úrovni uživatele. [Dokumentace Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

V místním terminálovém chatu Claude Code použijte vstup shellu k instalaci pouze pro Claude. Před spuštěním ověřte URL repozitáře. [Vstup shellu v Claude Code](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

V nové relaci zavolejte `$game-localization` v Codex nebo `/game-localization` v Claude Code. Při ruční instalaci zkopírujte celou složku `game-localization/` do `.claude/skills/` v projektu nebo `~/.claude/skills/` uživatele. [Příručka dovedností Claude Code](https://code.claude.com/docs/en/skills)

V hostovaných verzích ChatGPT a Claude používejte funkce nahrání nebo instalace účtu. Zmínka v chatu vyvolá nainstalovanou dovednost. Pro sdílený instalační odkaz použijte katalog platformy nebo sdílejte dovednost či plugin v oprávněném pracovním prostoru. [Sdílení pluginů ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Sdílení dovedností Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Používání dovednosti

1. Přiložte zdrojový text či soubor a aktuální glosář projektu pro cílové jazyky. Pokud glosář chybí, výslovně požádejte o návrh.
2. Uveďte zdrojový a cílové jazyky, platformu, typ materiálu a výstupní formát. Podle potřeby připojte limity znaků, snímky, poznámky o mluvčích nebo příklady proměnných.
3. U tabulek uveďte zdrojové a cílové sloupce a požádejte o kopii. U textů hry dodejte stabilní ID nebo klíče. U textů obchodu uveďte cílové pole a případný pevný limit.
4. V samostatné předávací zprávě zjistíte, zda je výsledek připravený k použití, nebo je zatím pracovní verzí. Zpráva uvádí zvlášť kontrolu souboru, jazykovou kontrolu a kontrolu ve hře nebo náhledu obchodu. U každého otevřeného problému najdete další krok. Před opětovným použitím schvalte termíny v projektovém glosáři.

U herního rozhraní obsahuje předávací zpráva kontroly seřazené podle priority. U každé uvádí obrazovku, ID řetězce, postup a podmínku úspěchu. Nejdřív se kontrolují dlouhé dosazené hodnoty a text, který se může oříznout. Pokud je známé písmo a využitelná šířka, dovednost může odhadnout potřebné místo. [Kontroly ve hře](../game-localization/references/in-build-qa.md)

Použijte [šablonu projektového glosáře](../game-localization/references/project-glossary-template.md), ve které jsou schválené termíny oddělené od návrhů. Uložte aktualizovaný soubor a přiložte jej k dalšímu chatu.

**Ukázková výzva pro tabulku**

~~~text
Pomocí Game Localization přelož sloupec ENGLISH v přiloženém sešitu do němčiny (de-DE). Zapiš překlady do GERMAN v nové kopii .xlsx. Vycházej z přiloženého glosáře a sloupce DESCRIPTION. Zachovej klíče, zdrojové sloupce, zástupné symboly a značky. Uveď dotazy k terminologii a výsledky kontrol zvlášť s ID řádků.
~~~

U podporovaných souborů `.xlsx` uveďte list, řádek záhlaví, sloupec se stálými ID, zdrojový sloupec a existující cílový sloupec. S Pythonem 3.9 nebo novějším dovednost zapisuje překlady podle ID do nové kopie a ověřuje zachování zbytku sešitu. Pokud sešit nelze ověřit, může nabídnout CSV s ID. [Pokyny pro Excel](../game-localization/references/xlsx-qa.md)

**Ukázková výzva pro stránku obchodu**

~~~text
Pomocí Game Localization přelož tento krátký popis na Steam z angličtiny do brazilské portugalštiny (pt-BR). Podle potřeby založ návrh glosáře. Zachovej název hry a dodrž zadaný limit znaků. Vrať text obchodu a samostatnou předávací zprávu.
~~~

### Kontrola překladů v CSV

U CSV se stálými ID řádků uveďte názvy sloupců s ID, zdrojovým textem a překladem. Je-li k dispozici Python 3.9 nebo novější, dovednost porovná zdrojový soubor se souborem překladu a upozorní na chybějící nebo duplicitní ID, prázdné překlady, změny podporovaných zástupných symbolů či značek a překročení limitů délky. [Pokyny ke kontrole CSV](../game-localization/references/csv-qa.md)

Vyzkoušejte [úvodní příklad s 12 řádky](../game-localization/examples/first-run/README.md) s pracovním překladem, schváleným glosářem a ukázkovou předávací zprávou.

### Naše nastavení modelů

| Prostředí | Model | Úroveň uvažování |
| --- | --- | --- |
| ChatGPT Work nebo Codex | GPT-6.1 Sol | High nebo vyšší, je-li dostupná |
| Claude | Claude Opus 5.5 | High nebo vyšší, je-li dostupná |

**High+** znamená High nebo vyšší úroveň dostupnou v aplikaci. Model a úroveň vyberte v aplikaci. Dovednost funguje nezávisle na této volbě. [Nastavení modelů OpenAI](https://learn.chatgpt.com/docs/models) · [Úrovně uvažování Claude](https://platform.claude.com/docs/en/build-with-claude/effort)

## Aktualizace a odstranění

| Způsob instalace | Aktualizace | Odstranění |
| --- | --- | --- |
| Plugin ChatGPT nebo Codex | Pokud spravujete nahraný soubor, zvolte **Upload new version** v podrobnostech pluginu. Instalace z katalogu nebo pracovního prostoru se aktualizují z daného zdroje. | Otevřete **Plugins → Installed → Game Localization** a zvolte **Uninstall plugin**, pokud je k dispozici. U spravované instalace kontaktujte správce. |
| Samostatná dovednost ChatGPT | Ve správě dovedností nahraďte osobní nahrávku nejnovějším samostatným ZIPem. | Otevřete **Plugins → Skills**, najděte dovednost v **Installed** či **Created by me** a použijte dostupnou volbu odstranění. Dovednosti pracovního prostoru spravuje správce. |
| Vlastní dovednost Claude | Nahrajte nový samostatný ZIP ze stránky správy. Pokud vznikne druhá položka, starší verzi vypněte. | Otevřete dovednost v **Customize → Skills** nebo **Plugins** a vypněte ji. Pro vlastní nahrávku zvolte **⋯ → Delete** a potvrďte. |
| Místní dovednost ze Skills CLI | Pro sledovanou větev spusťte `npx skills update game-localization` nebo instalujte z nové značky. | Ve stejném projektu spusťte `npx skills remove game-localization`. Při globální instalaci přidejte `-g`. |
| Místní složka nebo Codex Skill Installer | Nahraďte složku `game-localization/` nejnovější verzí. | Odstraňte `game-localization/`. Codex ji načítá z `.agents/skills/`, `~/.agents/skills/` nebo `~/.codex/skills/`. Claude Code používá `.claude/skills/` nebo `~/.claude/skills/`. Podle potřeby zahajte novou relaci. |

[Správa pluginů OpenAI](https://learn.chatgpt.com/docs/plugins) · [Správa vlastních dovedností Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Zdrojové soubory a balíčky

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) určuje, kdy se dovednost používá a jak zpracuje dávku.
- [`game-localization/references/`](../game-localization/references/) obsahuje pravidla a jazykové verze glosáře.
- [`packaging/chatgpt/`](../packaging/chatgpt/) obsahuje manifest a ikonu pluginu.
- [`packages/`](../packages/) obsahuje archivy připravené k nahrání.

Oba ZIPy vytvoříte ze stejného zdroje příkazem `python scripts/package.py` v kořeni repozitáře s Python 3.9 nebo novějším. Verze vychází z manifestu pluginu ChatGPT. Před distribucí nahrajte každý ZIP do odpovídajícího produktu a ověřte malou dávku s glosářem a chráněným zástupným symbolem.

## Licence

Game Localization je k dispozici pod [licencí MIT](../LICENSE). Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## Podpora autora

Pokud Game Localization pomáhá vašemu týmu, můžete [podpořit Maled1kt přes DonationAlerts](https://www.donationalerts.com/r/maled1kt). Příspěvky jsou zcela dobrovolné.
