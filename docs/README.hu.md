# Game Localization

![Game Localization by Maled1kt](../assets/game-localization-banner.png)

[English](../README.md) · [Minden nyelv](../README.md#languages)

A Game Localization egy ügynökkészség videojátékok szövegeinek fordításához, szerkesztéséhez és ellenőrzéséhez a ChatGPT-ben, a Codexben és a Claude-ban. Menüket, oktatóanyagokat, párbeszédeket, feliratokat, áruházi szövegeket és projektdokumentációt kezel a Steam, a PlayStation, az Xbox és a mobiljátékok számára.

[Telepítés](#telepítés) · [A készség használata](#a-készség-használata) · [Frissítés vagy eltávolítás](#frissítés-vagy-eltávolítás) · [A szerző támogatása](#a-szerző-támogatása) · [Fejlesztési terv](../ROADMAP.md) · [Változásnapló](../CHANGELOG.md)

## Funkciók

- A projekt jóváhagyott terminológiáját alkalmazza, az új kifejezéseket pedig javaslatként rögzíti.
- Megőrzi a lokalizációs kulcsokat, a `{player_name}` és `%s` típusú helyőrzőket, a címkéket, a jelentéssel bíró sortöréseket és más védett elemeket.
- Ellenőrzi a megadott hosszkorlátokat, és külön kezeli a fordítást, a kérdéseket, a forrásszöveg javításait és a minőségellenőrzési megjegyzéseket.
- [30 nyelvből és változatból álló alaplistát](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages) kínál, és egyedi listákat is fogad.
- A [75 kifejezést tartalmazó kezdőszójegyzék mind a 30 nyelvhez és változathoz](../game-localization/references/glossary/README.md) közös angol meghatározásokat és fordítási javaslatokat ad.

A készség útmutatót és referenciafájlokat tartalmaz. Projekt-API-kulcs, csatlakozó és háttérszolgáltatás nélkül működik. A fájlszerkesztés a csevegésben elérhető eszközöktől függ. Kiadás előtt ellenőrizd a fordított felületet a játék buildjében, az áruházi szöveget pedig a platform előnézetében.

## Telepítés

| Környezet | Csomag |
| --- | --- |
| ChatGPT vagy Codex bővítményfeltöltési joggal | [ChatGPT-bővítmény ZIP](../packages/game-localization-chatgpt-v0.1.8.zip) |
| Claude vagy önálló készségek feltöltésére jogosult ChatGPT-munkatér | [Önálló készség ZIP](../packages/game-localization-skill-v0.1.8.zip) |
| Helyi Codex vagy Claude Code | [Telepítés a forrásmappából](#telepítés-helyi-ügynökökhöz-egyetlen-paranccsal) |

Nyisd meg a csomag hivatkozását a GitHubon, és válaszd a **Download raw file** lehetőséget. A ZIP-et kicsomagolás nélkül töltsd fel.

### ChatGPT és Codex

1. A webes ChatGPT-ben nyisd meg a fiók bővítményfeltöltési lehetőségét. A jogosult tulajdonosok és rendszergazdák használhatják az **Admin console → Plugins → Add → Upload plugin** útvonalat.
2. Válaszd a bővítmény ZIP-fájlját. Az ellenőrzés után nyisd meg a **Game Localization** elemet a **Plugins** alatt, és válaszd az **Install plugin** lehetőséget, ha elérhető. A személyes feltöltés megjelenhet a **Personal → Created by me** alatt.
3. Indíts új csevegést a ChatGPT-ben vagy a Codexben. Írd be a `@` jelet, és válaszd a **Game Localization** elemet.

Ha a munkatér támogatja az önálló készségeket, töltsd fel a ZIP-et a **Plugins → Skills → Create → Upload from your computer** útvonalon. Várd meg az ellenőrzést, majd kövesd az utasításokat. A lehetőségek a fióktól és a munkatértől függenek. [OpenAI bővítményútmutató](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [OpenAI készségútmutató](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. A Claude beállításaiban kapcsold be a **Code execution and file creation** lehetőséget, ha a fiók vagy a munkatér megköveteli.
2. A webes Claude-ban vagy a Claude Desktopban nyisd meg a **Customize → Skills** menüt. Az új felületen az oldalsáv **Plugins** pontjában, a **Your plugins** alatt találod a kezelőszerveket.
3. Válaszd a **+ → Create skill → Upload a skill** lehetőséget és az önálló ZIP-et. Kapcsold be a `game-localization` készséget, amikor megjelenik.
4. Indíts új csevegést, és kérd meg Claude-ot a **Game Localization** használatára. Ha a készség megjelenik a beviteli mező **+** vagy **/** menüjében, válaszd ki ott.

Felügyelt munkatérben előfordulhat, hogy a rendszergazdának kell engedélyeznie vagy feltöltenie a készségeket. [Claude készségútmutató](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Claude új oldalsávja](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### Telepítés helyi ügynökökhöz egyetlen paranccsal

A parancsok a [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization) `main` ágát használják. A tároló és az ág közzététele után működnek. A relatív ZIP-hivatkozások más ágakon, címkéken és forkokban is használhatók.

A helyi Codex-csevegésben válaszd a beépített `$skill-installer` eszközt, és küldd el az alábbi kérést. Ha szükséges, engedélyezd a hálózati hozzáférést, majd indíts új munkamenetet. [Codex készségútmutató](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

A külső Skills CLI egyetlen terminálparanccsal telepíti ugyanazt a forrásmappát a helyi Codex és a Claude Code számára. Node.js 22.20 vagy újabb verzióval futtasd a célprojektből. Csak a szükséges ügynökök `-a` kapcsolóit tartsd meg. Felhasználói szintű telepítéshez add hozzá a `-g` kapcsolót. [Skills CLI dokumentáció](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

A helyi Claude Code terminálcsevegésében a shell bemenetével telepíthetsz csak a Claude számára. Futtatás előtt ellenőrizd a tároló URL-jét. [Shell bemenet a Claude Code-ban](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

Új munkamenetben hívd meg a `$game-localization` készséget a Codexben vagy a `/game-localization` parancsot a Claude Code-ban. Kézi telepítéshez másold a teljes `game-localization/` mappát a projekt `.claude/skills/` mappájába vagy a felhasználói `~/.claude/skills/` mappába. [Claude Code készségútmutató](https://code.claude.com/docs/en/skills)

A hosztolt ChatGPT-ben és Claude-ban a fiók feltöltési vagy telepítési lehetőségeit használd. A csevegésbeli említés elindítja a telepített készséget. Megosztható telepítési hivatkozáshoz közzéteheted a platform katalógusában, vagy megoszthatod a készséget vagy bővítményt egy megfelelő munkatérben. [ChatGPT-bővítmények megosztása](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Claude-készségek megosztása](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## A készség használata

1. Csatold a forrásszöveget vagy fájlt és a célnyelvek aktuális projektszójegyzékét. Ha nincs szójegyzék, kifejezetten kérj tervezetet.
2. Add meg a forrás- és célnyelveket, a platformot, az anyag típusát és a kimeneti formátumot. Szükség szerint adj meg karakterkorlátot, képernyőképet, beszélőre vonatkozó megjegyzést vagy változópéldát.
3. Táblázatnál nevezd meg a forrás- és céloszlopokat, és kérj új másolatot. Játékszövegnél adj meg állandó azonosítókat vagy kulcsokat. Áruházi szövegnél nevezd meg a célmezőt és az esetleges kötelező hosszkorlátot.
4. A külön átadási jegyzetből megtudhatod, hogy az eredmény használatra kész vagy még tervezet. A jegyzet külön mutatja a fájlellenőrzést, a nyelvi ellenőrzést és a játékban vagy az áruház előnézetében végzett ellenőrzést. Minden nyitott problémához megadja a következő lépést. Újrafelhasználás előtt hagyd jóvá a kifejezéseket a projekt szójegyzékében.

A [projektszójegyzék-sablonban](../game-localization/references/project-glossary-template.md) külön tarthatod a jóváhagyott kifejezéseket és a javaslatokat. Mentsd el a frissített fájlt, és csatold a következő beszélgetéshez.

**Példa táblázathoz**

~~~text
A Game Localization segítségével fordítsd le a mellékelt munkafüzet ENGLISH oszlopát németre (de-DE). A fordítást új .xlsx-másolatban a GERMAN oszlopba írd. Használd a mellékelt szójegyzéket és a DESCRIPTION oszlopot háttérként. Őrizd meg a kulcsokat, a forrásoszlopokat, a helyőrzőket és a címkéket. A terminológiai kérdéseket és az ellenőrzéseket külön sorold fel a sorazonosítókkal együtt.
~~~

Támogatott `.xlsx`-fájloknál add meg a munkalapot, a fejlécsor számát, az állandó azonosítók oszlopát, a forrásoszlopot és a már létező céloszlopot. Python 3.9 vagy újabb verzió esetén a készség az azonosítók alapján új másolatba írja a fordításokat, és ellenőrzi, hogy a munkafüzet többi része megmaradt-e. Ha a munkafüzet nem ellenőrizhető, azonosítókat tartalmazó CSV-fájlt ajánlhat. [Excel-útmutató](../game-localization/references/xlsx-qa.md)

**Példa áruházi oldalhoz**

~~~text
A Game Localization segítségével lokalizáld ezt a rövid Steam-leírást angolról brazíliai portugálra (pt-BR). Szükség esetén készíts szójegyzéktervezetet. Őrizd meg a játék címét, és tartsd be a karakterkorlátot. Az áruházi szöveget és az átadási jegyzetet külön add vissza.
~~~

### CSV-fordítások ellenőrzése

Ha a CSV-fájl sorai állandó azonosítóval rendelkeznek, adja meg az azonosítót, a forrásszöveget és a fordítást tartalmazó oszlop fejlécét. Python 3.9 vagy újabb verzió esetén a készség összehasonlítja a forrásfájlt a lefordított fájllal, és jelzi a hiányzó vagy ismétlődő azonosítókat, az üres fordításokat, a támogatott helyőrzők vagy címkék változásait és a hosszkorlátok túllépését. [Útmutató a CSV-ellenőrzéshez](../game-localization/references/csv-qa.md)

Próbáld ki a [12 soros kezdőpéldát](../game-localization/examples/first-run/README.md), amelyhez fordítástervezet, jóváhagyott szójegyzék és minta átadási jegyzet tartozik.

### Az általunk használt modellbeállítások

| Környezet | Modell | Következtetési szint |
| --- | --- | --- |
| ChatGPT Work vagy Codex | GPT-6.1 Sol | High vagy magasabb, ha elérhető |
| Claude | Claude Opus 5.5 | High vagy magasabb, ha elérhető |

A **High+** a kliensben elérhető High vagy magasabb szintet jelöli. A modellt és a szintet a kliensben válaszd ki. A készség ettől a választástól függetlenül működik. [OpenAI modellbeállítások](https://learn.chatgpt.com/docs/models) · [Claude következtetési szintek](https://platform.claude.com/docs/en/build-with-claude/effort)

## Frissítés vagy eltávolítás

| Telepítési mód | Frissítés | Eltávolítás |
| --- | --- | --- |
| ChatGPT- vagy Codex-bővítmény | Ha te kezeled a feltöltést, a részleteknél válaszd az **Upload new version** lehetőséget. A katalógusból vagy munkatérből telepített bővítmények onnan kapnak frissítést. | Nyisd meg a **Plugins → Installed → Game Localization** útvonalat, és válaszd az **Uninstall plugin** lehetőséget, ha elérhető. Felügyelt telepítésnél kérdezd a rendszergazdát. |
| Önálló ChatGPT-készség | A készségkezelőben cseréld le a személyes feltöltést a legfrissebb önálló ZIP-re. | A **Plugins → Skills** menüben keresd meg a készséget az **Installed** vagy a **Created by me** alatt. Használd az eltávolítási lehetőséget. A munkatér készségeit a rendszergazdák kezelik. |
| Egyéni Claude-készség | A kezelőoldalon töltsd fel az új önálló ZIP-et. Ha újabb bejegyzés jön létre, kapcsold ki a korábbi verziót. | Nyisd meg a **Customize → Skills** vagy **Plugins** alatt, és kapcsold ki. Saját feltöltésnél válaszd a **⋯ → Delete** lehetőséget, majd erősítsd meg. |
| Skills CLI-vel telepített helyi készség | Követett ágnál futtasd a `npx skills update game-localization` parancsot, vagy telepíts az új címkéről. | Ugyanabban a projektben futtasd a `npx skills remove game-localization` parancsot. Globális telepítésnél add hozzá a `-g` kapcsolót. |
| Helyi mappa vagy Codex Skill Installer | Cseréld a telepített `game-localization/` mappát a legújabbra. | Töröld a `game-localization/` mappát. A Codex a `.agents/skills/`, `~/.agents/skills/` vagy `~/.codex/skills/` útvonalról töltheti be. A Claude Code útvonalai `.claude/skills/` és `~/.claude/skills/`. Szükség esetén indíts új munkamenetet. |

[OpenAI-bővítmények kezelése](https://learn.chatgpt.com/docs/plugins) · [Egyéni Claude-készségek kezelése](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Forráskód és csomagolás

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) meghatározza, mikor fut a készség, és hogyan dolgozza fel a szövegeket.
- [`game-localization/references/`](../game-localization/references/) tartalmazza a szabályokat és a nyelvi szójegyzékeket.
- [`packaging/chatgpt/`](../packaging/chatgpt/) tartalmazza a bővítmény jegyzékfájlját és ikonját.
- [`packages/`](../packages/) tartalmazza a feltöltésre kész archívumokat.

Mindkét ZIP újraépítéséhez futtasd a `python scripts/package.py` parancsot a tároló gyökerében Python 3.9 vagy újabb verzióval. A verzió a ChatGPT-bővítmény jegyzékfájljából származik. Terjesztés előtt töltsd fel mindkét ZIP-et a megfelelő termékbe, és tesztelj egy kisebb szövegcsomagot szójegyzékkel és védett helyőrzővel.

## Licenc

A Game Localization az [MIT licenc](../LICENSE) alatt érhető el. Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## A szerző támogatása

Ha a Game Localization segíti a csapatodat, [támogathatod Maled1ktet a DonationAlerts felületén](https://www.donationalerts.com/r/maled1kt). A támogatás önkéntes.
