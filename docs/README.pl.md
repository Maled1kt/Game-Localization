# Game Localization

![Game Localization by Maled1kt](../assets/game-localization-banner.png)

[English](../README.md) · [Wszystkie języki](../README.md#languages)

Game Localization to umiejętność agenta do tłumaczenia, redagowania i sprawdzania tekstów gier w ChatGPT, Codex i Claude. Obsługuje menu, samouczki, dialogi, napisy, teksty sklepowe i dokumentację projektową dla Steam, PlayStation, Xbox i gier mobilnych.

[Instalacja](#instalacja) · [Korzystanie z umiejętności](#korzystanie-z-umiejętności) · [Aktualizacja i usuwanie](#aktualizacja-i-usuwanie) · [Wesprzyj autora](#wesprzyj-autora) · [Plan rozwoju](../ROADMAP.md) · [Historia zmian](../CHANGELOG.md)

## Funkcje

- Stosuje zatwierdzoną terminologię projektu i zapisuje nowe terminy jako propozycje.
- Zachowuje klucze lokalizacyjne, symbole zastępcze takie jak `{player_name}` i `%s`, znaczniki, istotne podziały wierszy i pozostałe elementy chronione.
- Sprawdza podane limity długości i oddziela przekład od pytań, poprawek źródła oraz uwag z kontroli jakości.
- Oferuje [zestaw 30 języków i wariantów](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages) oraz obsługuje własne listy.
- Zawiera [glosariusz startowy 75 terminów we wszystkich 30 językach i wariantach](../game-localization/references/glossary/README.md), ze wspólnymi definicjami angielskimi i propozycjami tłumaczeń.

Umiejętność zawiera instrukcje i pliki referencyjne. Działa bez klucza API projektu, łącznika ani usługi w tle. Edycja plików zależy od narzędzi dostępnych w czacie. Przed wydaniem sprawdź interfejs w kompilacji gry, a teksty sklepowe w podglądzie platformy.

## Instalacja

| Środowisko | Pakiet |
| --- | --- |
| ChatGPT lub Codex z uprawnieniem do przesyłania wtyczek | [ZIP wtyczki ChatGPT](../packages/game-localization-chatgpt-v0.1.12.zip) |
| Claude lub obszary robocze ChatGPT z uprawnieniem do przesyłania samodzielnych umiejętności | [ZIP samodzielnej umiejętności](../packages/game-localization-skill-v0.1.12.zip) |
| Lokalny Codex lub Claude Code | [Instalacja z katalogu źródłowego](#instalacja-dla-lokalnych-agentów-jednym-poleceniem) |

W lokalnym Codex i Claude Code można zainstalować Game Localization ze wspólnego katalogu GitHub. Instrukcja opisuje pierwszą instalację, przejście z ZIP i aktualizacje w każdym kliencie. [Katalog GitHub](plugin-catalog.md)

Otwórz odnośnik do pakietu w GitHub i wybierz **Download raw file**. Prześlij ZIP bez rozpakowywania.

### ChatGPT i Codex

1. W internetowej wersji ChatGPT otwórz opcję przesyłania wtyczek. Uprawnieni właściciele i administratorzy mogą użyć **Admin console → Plugins → Add → Upload plugin**.
2. Wybierz ZIP wtyczki. Po weryfikacji otwórz **Game Localization** w **Plugins** i wybierz **Install plugin**, jeśli jest dostępne. Własny plik może pojawić się w **Personal → Created by me**.
3. Otwórz nowy czat w ChatGPT lub Codex. Wpisz `@` i wybierz **Game Localization** z podpowiedzi.

Jeśli obszar roboczy obsługuje osobne umiejętności, prześlij ZIP przez **Plugins → Skills → Create → Upload from your computer**. Poczekaj na skanowanie i postępuj według wskazówek. Opcje zależą od konta i obszaru roboczego. [Poradnik wtyczek OpenAI](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Poradnik umiejętności OpenAI](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. Włącz **Code execution and file creation** w ustawieniach Claude, jeśli wymaga tego konto lub obszar roboczy.
2. W Claude w przeglądarce lub Claude Desktop otwórz **Customize → Skills**. W nowszym układzie otwórz **Plugins** na pasku bocznym i znajdź ustawienia w **Your plugins**.
3. Wybierz **+ → Create skill → Upload a skill** i samodzielny ZIP. Włącz `game-localization`, gdy się pojawi.
4. Otwórz nowy czat i poproś Claude o użycie **Game Localization**. Jeśli umiejętność pojawi się pod **+** lub **/** w polu wiadomości, wybierz ją tam.

W zarządzanym obszarze roboczym umiejętności może włączać lub przesyłać administrator. [Poradnik umiejętności Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Nowy pasek boczny Claude](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### Instalacja dla lokalnych agentów jednym poleceniem

Polecenia korzystają z gałęzi `main` repozytorium [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization). Zadziałają po opublikowaniu repozytorium i gałęzi. Względne odnośniki ZIP działają także w innych gałęziach, tagach i forkach.

W lokalnym czacie Codex wybierz wbudowane `$skill-installer` i wyślij poniższe żądanie. W razie potrzeby zezwól na dostęp do sieci i rozpocznij nową sesję. [Poradnik umiejętności Codex](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

Zewnętrzne narzędzie Skills CLI instaluje ten sam katalog dla lokalnego Codex i Claude Code jednym poleceniem. Uruchom je z docelowego projektu w Node.js 22.20 lub nowszym. Zostaw opcje `-a` potrzebnych agentów. Dodaj `-g`, aby zainstalować na poziomie użytkownika. [Dokumentacja Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

W lokalnym czacie terminalowym Claude Code użyj pola powłoki, aby zainstalować umiejętność tylko dla Claude. Przed uruchomieniem sprawdź adres URL repozytorium. [Wejście powłoki w Claude Code](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

W nowej sesji wywołaj `$game-localization` w Codex lub `/game-localization` w Claude Code. Do instalacji ręcznej skopiuj cały katalog `game-localization/` do `.claude/skills/` w projekcie lub `~/.claude/skills/` użytkownika. [Poradnik umiejętności Claude Code](https://code.claude.com/docs/en/skills)

W wersjach hostowanych ChatGPT i Claude użyj opcji przesyłania lub instalacji na koncie. Wzmianka w czacie wywołuje zainstalowaną umiejętność. Aby udostępnić odnośnik instalacyjny, opublikuj ją w katalogu platformy albo udostępnij umiejętność lub wtyczkę w uprawnionym obszarze roboczym. [Udostępnianie wtyczek ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Udostępnianie umiejętności Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Korzystanie z umiejętności

1. Dołącz tekst lub plik źródłowy oraz aktualny glosariusz projektu dla języków docelowych. Jeśli go brakuje, poproś wprost o wersję roboczą.
2. Podaj języki źródłowy i docelowe, platformę, typ materiału i format wyniku. W razie potrzeby dodaj limity znaków, zrzuty ekranu, informacje o postaciach lub przykłady zmiennych.
3. Dla arkusza wskaż kolumny źródłowe i docelowe oraz poproś o nową kopię. Dla tekstów gry podaj stałe identyfikatory lub klucze. Dla sklepu podaj pole docelowe i ewentualny sztywny limit.
4. Sprawdź w oddzielnym raporcie, czy wynik jest gotowy do użycia, czy nadal jest wersją roboczą. Raport osobno przedstawia kontrolę pliku, weryfikację językową i sprawdzenie w grze lub podglądzie sklepu. Dla każdego otwartego problemu wskazuje następny krok. Zatwierdź terminy w glosariuszu projektu przed ponownym użyciem.

W przypadku interfejsu gry raport przekazania zawiera listę kontroli według priorytetu. Każdy wpis podaje ekran, ID ciągu, kroki odtworzenia i kryterium zaliczenia. Najpierw sprawdzane są długie podstawiane wartości i tekst, który może zostać obcięty. Jeśli znane są krój pisma i dostępna szerokość, umiejętność może oszacować potrzebne miejsce. [Kontrole w grze](../game-localization/references/in-build-qa.md)

Użyj [szablonu glosariusza projektu](../game-localization/references/project-glossary-template.md), aby oddzielić zatwierdzone terminy od propozycji. Zapisz zaktualizowany plik i dołącz go do następnej rozmowy.

**Przykładowe polecenie dla arkusza**

~~~text
Użyj Game Localization, aby przetłumaczyć kolumnę ENGLISH załączonego skoroszytu na niemiecki (de-DE). Zapisz przekład w GERMAN w nowej kopii .xlsx. Wykorzystaj dołączony glosariusz i kolumnę DESCRIPTION. Zachowaj klucze, kolumny źródłowe, symbole zastępcze i znaczniki. Pytania terminologiczne i wyniki kontroli podaj oddzielnie z identyfikatorami wierszy.
~~~

W przypadku obsługiwanych plików `.xlsx` podaj arkusz, wiersz nagłówków, kolumnę ze stałymi identyfikatorami, kolumnę źródłową i istniejącą kolumnę docelową. Przy użyciu Pythona 3.9 lub nowszego umiejętność zapisuje tłumaczenia według ID w nowej kopii i sprawdza, czy reszta skoroszytu została zachowana. Jeśli nie można zweryfikować skoroszytu, może zaproponować plik CSV z identyfikatorami. [Instrukcje dla Excela](../game-localization/references/xlsx-qa.md)

**Przykładowe polecenie dla strony sklepu**

~~~text
Użyj Game Localization do lokalizacji tego krótkiego opisu Steam z angielskiego na portugalski brazylijski (pt-BR). W razie potrzeby utwórz roboczy glosariusz. Zachowaj tytuł gry i podany limit znaków. Zwróć tekst sklepowy oraz osobny raport.
~~~

Dla stron Steam umiejętność zwraca osobno krótki opis i sekcję „O tej grze”, sprawdza podane limity oraz informacje o grze i może przygotować wersję roboczą z obsługiwanego eksportu JSON ze Steamworks. Raport przekazania osobno podaje stan importu i podglądu. [Procedura dla stron Steam](../game-localization/references/steam-store.md)

### Sprawdzanie tłumaczeń w CSV

W przypadku pliku CSV ze stałymi identyfikatorami wierszy podaj nagłówki kolumn z identyfikatorem, tekstem źródłowym i tłumaczeniem. Jeśli dostępny jest Python 3.9 lub nowszy, umiejętność porówna plik źródłowy z plikiem tłumaczenia i wskaże brakujące lub powtarzające się identyfikatory, puste tłumaczenia, zmiany obsługiwanych symboli zastępczych lub znaczników oraz przekroczenia limitów długości. [Instrukcja sprawdzania plików CSV](../game-localization/references/csv-qa.md)

Aby zaktualizować tłumaczenie, załącz poprzedni i aktualny źródłowy plik CSV, zatwierdzone tłumaczenia oraz późniejsze poprawki redakcyjne. Umiejętność dopasowuje wiersze po ID, zachowuje odpowiednie tłumaczenia niezmienionych wierszy oraz wskazuje wiersze dodane, zmienione i usunięte. Przy długich dialogach zapisz postęp po każdej scenie, aby móc kontynuować pracę na tym samym pliku. [Aktualizacja tłumaczeń CSV](../game-localization/references/csv-updates.md)

Wypróbuj [przykład na początek z 12 wierszami](../game-localization/examples/first-run/README.md). Zawiera robocze tłumaczenie, zatwierdzony glosariusz i przykładowy raport.

### Nasze ustawienia modeli

| Środowisko | Model | Poziom rozumowania |
| --- | --- | --- |
| ChatGPT Work lub Codex | GPT-6.1 Sol | High lub wyższy, jeśli dostępny |
| Claude | Claude Opus 5.5 | High lub wyższy, jeśli dostępny |

**High+** oznacza High lub wyższy poziom dostępny w aplikacji. Wybierz model i poziom w aplikacji. Umiejętność działa niezależnie od tej preferencji. [Ustawienia modeli OpenAI](https://learn.chatgpt.com/docs/models) · [Poziomy rozumowania Claude](https://platform.claude.com/docs/en/build-with-claude/effort)

## Aktualizacja i usuwanie

| Sposób instalacji | Aktualizacja | Usuwanie |
| --- | --- | --- |
| Wtyczka ChatGPT lub Codex | Jeśli zarządzasz przesłanym plikiem, wybierz **Upload new version** w szczegółach wtyczki. Instalacje z katalogu lub obszaru roboczego aktualizują się z tego źródła. | Otwórz **Plugins → Installed → Game Localization** i wybierz **Uninstall plugin**, jeśli jest dostępne. W sprawie zarządzanej instalacji skontaktuj się z administratorem. |
| Samodzielna umiejętność ChatGPT | W zarządzaniu umiejętnościami zastąp osobisty plik najnowszym samodzielnym ZIP-em. | Otwórz **Plugins → Skills**, znajdź pozycję w **Installed** lub **Created by me** i użyj dostępnej opcji usuwania. Administrator zarządza umiejętnościami obszaru. |
| Niestandardowa umiejętność Claude | Prześlij nowy samodzielny ZIP w panelu zarządzania. Wyłącz poprzednią wersję, jeśli pojawi się druga pozycja. | Otwórz umiejętność w **Customize → Skills** lub **Plugins** i wyłącz ją. Dla własnego pliku wybierz **⋯ → Delete** i potwierdź. |
| Lokalna umiejętność z Skills CLI | Uruchom `npx skills update game-localization` dla śledzonej gałęzi lub zainstaluj z nowego tagu. | Uruchom `npx skills remove game-localization` w tym samym projekcie. Przy instalacji globalnej dodaj `-g`. |
| Lokalny katalog lub Codex Skill Installer | Zastąp katalog `game-localization/` najnowszą wersją. | Usuń `game-localization/`. Codex może go wczytać z `.agents/skills/`, `~/.agents/skills/` lub `~/.codex/skills/`. Claude Code używa `.claude/skills/` lub `~/.claude/skills/`. W razie potrzeby rozpocznij nową sesję. |

[Zarządzanie wtyczkami OpenAI](https://learn.chatgpt.com/docs/plugins) · [Zarządzanie niestandardowymi umiejętnościami Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Kod źródłowy i pakiety

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) określa, kiedy umiejętność się uruchamia i jak przetwarza partię tekstów.
- [`game-localization/references/`](../game-localization/references/) zawiera reguły i wersje językowe glosariusza startowego.
- [`packaging/chatgpt/`](../packaging/chatgpt/) zawiera manifest i ikonę wtyczki.
- [`packages/`](../packages/) zawiera archiwa gotowe do przesłania.

Aby zbudować oba ZIP-y z tego samego źródła, uruchom `python scripts/package.py` w katalogu głównym repozytorium przy użyciu Python 3.9 lub nowszego. Wersja pochodzi z manifestu wtyczki ChatGPT. Przed dystrybucją prześlij każdy ZIP do właściwego produktu i sprawdź małą partię z glosariuszem i chronionym symbolem zastępczym.

## Licencja

Game Localization jest dostępne na [licencji MIT](../LICENSE). Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## Wesprzyj autora

Jeśli Game Localization pomaga twojemu zespołowi, możesz [wesprzeć Maled1kt przez DonationAlerts](https://www.donationalerts.com/r/maled1kt). Wpłaty są całkowicie dobrowolne.
