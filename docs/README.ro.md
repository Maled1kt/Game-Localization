# Game Localization

![Banner Game Localization cu două ferestre de dialog din joc care fac schimb de caractere din limbi diferite](../assets/game-localization-banner.png)

[English](../README.md) · [Toate limbile](../README.md#languages)

Game Localization este o competență pentru agenți care traduce, editează și verifică texte de joc în ChatGPT, Codex și Claude. Acoperă meniuri, tutoriale, dialoguri, subtitrări, texte de magazin și documentație de proiect pentru Steam, PlayStation, Xbox și jocuri mobile.

[Instalare](#instalare) · [Folosirea competenței](#folosirea-competenței) · [Actualizare sau eliminare](#actualizare-sau-eliminare) · [Sprijină autorul](#sprijină-autorul) · [Plan de dezvoltare](../ROADMAP.md) · [Istoricul modificărilor](../CHANGELOG.md)

## Funcții

- Aplică terminologia aprobată a proiectului și înregistrează termenii noi ca propuneri.
- Păstrează cheile de localizare, substituenții precum `{player_name}` și `%s`, etichetele, întreruperile de linie relevante și alte elemente protejate.
- Verifică limitele de lungime și separă traducerea de întrebări, corecturi ale sursei și note de control al calității.
- Oferă [o listă predefinită de 30 de limbi și variante](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages) și acceptă liste personalizate.
- Include [un glosar inițial de 75 de termeni în toate cele 30 de limbi și variante](../game-localization/references/glossary/README.md), cu definiții comune în engleză și propuneri de traducere.

Competența conține instrucțiuni și fișiere de referință. Funcționează fără cheie API de proiect, conector sau serviciu în fundal. Editarea fișierelor depinde de instrumentele din conversație. Înainte de lansare, verifică interfața în versiunea compilată a jocului și textele în previzualizarea magazinului de pe platformă.

## Instalare

| Mediu | Pachet |
| --- | --- |
| ChatGPT sau Codex cu permisiunea de a încărca pluginuri | [ZIP al pluginului ChatGPT](../packages/game-localization-chatgpt-v0.1.5.zip) |
| Claude sau spații ChatGPT care permit încărcarea competențelor independente | [ZIP al competenței independente](../packages/game-localization-skill-v0.1.5.zip) |
| Codex local sau Claude Code | [Instalare din folderul sursă](#instalare-pentru-agenți-locali-cu-o-singură-comandă) |

Deschide linkul pachetului pe GitHub și alege **Download raw file**. Încarcă ZIP-ul fără să-l dezarhivezi.

### ChatGPT și Codex

1. În ChatGPT pe web, deschide opțiunea de încărcare a pluginurilor pentru cont. Proprietarii și administratorii autorizați pot folosi **Admin console → Plugins → Add → Upload plugin**.
2. Alege ZIP-ul pluginului. După validare, deschide **Game Localization** în **Plugins** și alege **Install plugin** dacă apare. Încărcările personale pot apărea în **Personal → Created by me**.
3. Deschide o conversație nouă în ChatGPT sau Codex. Tastează `@` și selectează **Game Localization** dintre sugestii.

Dacă spațiul acceptă competențe independente, încarcă ZIP-ul prin **Plugins → Skills → Create → Upload from your computer**. Așteaptă scanarea și urmează indicațiile. Opțiunile depind de cont și de spațiul de lucru. [Ghid OpenAI pentru pluginuri](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Ghid OpenAI pentru competențe](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. Activează **Code execution and file creation** în setările Claude dacă este necesar pentru cont sau spațiu.
2. În Claude pe web sau Claude Desktop, deschide **Customize → Skills**. În interfața nouă, deschide **Plugins** din bara laterală și caută opțiunile în **Your plugins**.
3. Alege **+ → Create skill → Upload a skill** și ZIP-ul independent. Activează `game-localization` când apare.
4. Deschide o conversație nouă și cere-i lui Claude să folosească **Game Localization**. Dacă apare sub **+** sau **/** în câmpul de mesaj, selecteaz-o acolo.

Într-un spațiu administrat, activarea sau încărcarea competențelor poate necesita un administrator. [Ghid Claude pentru competențe](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Noua bară laterală Claude](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### Instalare pentru agenți locali cu o singură comandă

Comenzile folosesc ramura `main` din [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization). Vor funcționa după publicarea depozitului și a ramurii. Linkurile ZIP relative funcționează și în alte ramuri, etichete și forkuri.

Într-o conversație locală Codex, selectează `$skill-installer` și trimite solicitarea de mai jos. Aprobă accesul la rețea dacă ți se cere, apoi deschide o sesiune nouă. [Ghid Codex pentru competențe](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

Utilitarul terț Skills CLI poate instala același folder sursă pentru Codex local și Claude Code cu o comandă. Ruleaz-o din proiectul țintă cu Node.js 22.20 sau mai nou. Păstrează opțiunile `-a` pentru agenții necesari. Adaugă `-g` pentru instalare la nivel de utilizator. [Referință Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

În conversația din terminalul local Claude Code, folosește câmpul shell pentru instalarea doar în Claude. Verifică URL-ul depozitului înainte de rulare. [Intrare shell în Claude Code](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

Într-o sesiune nouă, apelează `$game-localization` în Codex sau `/game-localization` în Claude Code. Pentru instalare manuală, copiază folderul `game-localization/` integral în `.claude/skills/` din proiect sau în `~/.claude/skills/` pentru utilizator. [Ghid Claude Code pentru competențe](https://code.claude.com/docs/en/skills)

În versiunile găzduite ChatGPT și Claude, folosește opțiunile de încărcare sau instalare ale contului. O mențiune în conversație apelează competența instalată. Pentru un link partajabil, publică în catalogul platformei sau partajează competența ori pluginul într-un spațiu eligibil. [Partajarea pluginurilor ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Partajarea competențelor Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Folosirea competenței

1. Atașează textul sau fișierul sursă și glosarul actual al proiectului pentru limbile țintă. Dacă nu există, cere explicit o versiune provizorie.
2. Precizează limbile sursă și țintă, platforma, tipul de material și formatul rezultatului. Adaugă, dacă este relevant, limite de caractere, capturi, note despre vorbitori sau exemple de variabile.
3. Pentru foi de calcul, indică coloanele sursă și țintă și cere o copie nouă. Pentru texte de joc, furnizează identificatori sau chei stabile. Pentru magazin, indică câmpul și limita strictă de lungime, dacă există.
4. Consultă raportul de predare separat ca să vezi dacă rezultatul este gata de folosit sau încă în stadiu de ciornă. Raportul prezintă separat verificarea fișierului, revizuirea lingvistică și verificarea în joc sau în previzualizarea magazinului. Pentru fiecare problemă deschisă, indică pasul următor. Aprobă termenii în glosarul proiectului înainte de a-i refolosi.

**Exemplu de solicitare pentru o foaie de calcul**

~~~text
Folosește Game Localization pentru a traduce coloana ENGLISH a registrului atașat în germană (de-DE). Scrie traducerile în GERMAN într-o copie .xlsx nouă. Folosește glosarul atașat și coloana DESCRIPTION pentru context. Păstrează cheile, coloanele sursă, substituenții și etichetele. Listează separat întrebările terminologice și verificările, cu ID-urile rândurilor.
~~~

**Exemplu de solicitare pentru o pagină de magazin**

~~~text
Folosește Game Localization pentru a localiza această descriere scurtă Steam din engleză în portugheză braziliană (pt-BR). Creează un glosar provizoriu dacă este necesar. Păstrează titlul jocului și respectă limita de caractere indicată. Livrează textul magazinului și un raport separat.
~~~

### Verificarea traducerilor în CSV

Pentru un fișier CSV cu ID-uri stabile pentru rânduri, specificați anteturile coloanelor pentru ID, textul sursă și traducere. Dacă este disponibil Python 3.9 sau o versiune ulterioară, competența compară fișierul sursă cu cel tradus și semnalează ID-urile lipsă sau duplicate, traducerile goale, modificările aduse substituenților sau etichetelor acceptate și depășirile limitelor de lungime. [Instrucțiuni pentru verificarea fișierelor CSV](../game-localization/references/csv-qa.md)

### Setările de model pe care le folosim

| Mediu | Model | Nivel de raționament |
| --- | --- | --- |
| ChatGPT Work sau Codex | GPT-6.1 Sol | High sau mai ridicat, dacă este disponibil |
| Claude | Claude Opus 5.5 | High sau mai ridicat, dacă este disponibil |

**High+** înseamnă High sau un nivel superior disponibil în aplicație. Alege modelul și nivelul în aplicație. Competența funcționează independent de această alegere. [Setări modele OpenAI](https://learn.chatgpt.com/docs/models) · [Niveluri de raționament Claude](https://platform.claude.com/docs/en/build-with-claude/effort)

## Actualizare sau eliminare

| Mod de instalare | Actualizare | Eliminare |
| --- | --- | --- |
| Plugin ChatGPT sau Codex | Dacă gestionezi încărcarea, alege **Upload new version** în detaliile pluginului. Instalările din catalog sau spațiu primesc actualizări de la sursa respectivă. | Deschide **Plugins → Installed → Game Localization** și alege **Uninstall plugin** dacă este disponibil. Pentru o instalare administrată, contactează administratorul. |
| Competență ChatGPT independentă | Înlocuiește încărcarea personală cu ultimul ZIP independent din secțiunea de gestionare. | Deschide **Plugins → Skills**, caută sub **Installed** sau **Created by me** și folosește opțiunea de eliminare disponibilă. Administratorii gestionează competențele spațiului. |
| Competență Claude personalizată | Încarcă noul ZIP din pagina de gestionare. Dacă apare o a doua intrare, dezactivează versiunea anterioară. | Deschide în **Customize → Skills** sau **Plugins** și dezactivează competența. Pentru încărcarea proprie, alege **⋯ → Delete** și confirmă. |
| Competență locală instalată prin Skills CLI | Rulează `npx skills update game-localization` pentru o ramură urmărită sau instalează din eticheta nouă. | Rulează `npx skills remove game-localization` din același proiect. Adaugă `-g` dacă instalarea a fost globală. |
| Folder local sau Codex Skill Installer | Înlocuiește folderul `game-localization/` cu ultima versiune. | Șterge `game-localization/`. Codex poate încărca din `.agents/skills/`, `~/.agents/skills/` sau `~/.codex/skills/`. Claude Code folosește `.claude/skills/` sau `~/.claude/skills/`. Pornește o sesiune nouă dacă este necesar. |

[Gestionarea pluginurilor OpenAI](https://learn.chatgpt.com/docs/plugins) · [Gestionarea competențelor Claude personalizate](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Cod sursă și împachetare

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) definește când rulează competența și cum procesează un lot.
- [`game-localization/references/`](../game-localization/references/) conține regulile și edițiile glosarului pe limbi.
- [`packaging/chatgpt/`](../packaging/chatgpt/) conține manifestul și pictograma pluginului.
- [`packages/`](../packages/) conține arhivele gata de încărcat.

Pentru a reconstrui ambele ZIP-uri din aceeași sursă, rulează `python scripts/package.py` din rădăcina depozitului cu Python 3.9 sau mai nou. Versiunea provine din manifestul pluginului ChatGPT. Înainte de distribuire, încarcă fiecare ZIP în produsul potrivit și testează un lot mic cu glosar și substituent protejat.

## Licență

Game Localization este disponibil sub [licența MIT](../LICENSE). Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## Sprijină autorul

Dacă Game Localization îți ajută echipa, îl poți [sprijini pe Maled1kt prin DonationAlerts](https://www.donationalerts.com/r/maled1kt). Donațiile sunt complet voluntare.
