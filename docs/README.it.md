# Game Localization

![Game Localization by Maled1kt](../assets/game-localization-banner.png)

[English](../README.md) · [Tutte le lingue](../README.md#languages)

Game Localization è una skill per agenti che traduce, revisiona e verifica testi di videogiochi in ChatGPT, Codex e Claude. È pensata per menu, tutorial, dialoghi, sottotitoli, testi del negozio e documentazione per Steam, PlayStation, Xbox e giochi per dispositivi mobili.

[Installazione](#installazione) · [Usare la skill](#usare-la-skill) · [Aggiornare o rimuovere](#aggiornare-o-rimuovere) · [Sostenere l’autore](#sostenere-lautore) · [Piano di sviluppo](../ROADMAP.md) · [Registro delle modifiche](../CHANGELOG.md)

## Funzionalità

- Applica la terminologia approvata del progetto e registra i nuovi termini come proposte.
- Preserva chiavi di localizzazione, segnaposto come `{player_name}` e `%s`, tag, interruzioni di riga significative e altri elementi protetti.
- Verifica i limiti di lunghezza e separa la traduzione da domande, correzioni del sorgente e note sul controllo qualità.
- Offre un [elenco predefinito di 30 lingue e varianti](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages) e accetta elenchi personalizzati.
- Include un [glossario di 75 termini in tutte le 30 lingue e varianti](../game-localization/references/glossary/README.md), con definizioni comuni in inglese e proposte di traduzione.

La skill contiene istruzioni e riferimenti. Funziona senza chiavi API di progetto, connettori o servizi in background. La modifica dei file dipende dagli strumenti della chat. Prima del rilascio verifica l’interfaccia nella build e i testi del negozio nell’anteprima della piattaforma.

## Installazione

| Ambiente | Pacchetto |
| --- | --- |
| ChatGPT o Codex con autorizzazione al caricamento dei plugin | [ZIP del plugin ChatGPT](../packages/game-localization-chatgpt-v0.1.10.zip) |
| Claude o spazi ChatGPT abilitati al caricamento di skill autonome | [ZIP della skill autonoma](../packages/game-localization-skill-v0.1.10.zip) |
| Codex locale o Claude Code | [Installa dalla cartella sorgente](#installazione-locale-con-un-comando) |

Su GitHub apri il link del pacchetto e scegli **Download raw file**. Carica lo ZIP senza estrarlo.

### ChatGPT e Codex

1. In ChatGPT sul Web apri l’opzione di caricamento dei plugin. I titolari e gli amministratori autorizzati possono usare **Admin console → Plugins → Add → Upload plugin**.
2. Seleziona lo ZIP del plugin. Dopo la convalida, apri **Game Localization** in **Plugins** e scegli **Install plugin**, se disponibile. Un caricamento personale può apparire in **Personal → Created by me**.
3. Apri una nuova chat in ChatGPT o Codex. Digita `@` e seleziona **Game Localization**.

Se lo spazio consente skill autonome, vai a **Plugins → Skills → Create → Upload from your computer** e carica lo ZIP corrispondente. Attendi la scansione e segui le indicazioni. Le opzioni dipendono dall’account e dallo spazio di lavoro. [Guida ai plugin OpenAI](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Guida alle skill OpenAI](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. Abilita **Code execution and file creation** nelle impostazioni di Claude se l’account o lo spazio lo richiede.
2. In Claude sul Web o in Claude Desktop apri **Customize → Skills**. Nella nuova interfaccia apri **Plugins** dalla barra laterale e cerca i controlli in **Your plugins**.
3. Scegli **+ → Create skill → Upload a skill** e lo ZIP autonomo. Attiva `game-localization` quando compare.
4. Apri una nuova chat e chiedi a Claude di usare **Game Localization**. Se compare tra le opzioni **+** o **/** della casella di composizione, selezionala lì.

Negli spazi gestiti può essere necessario che un amministratore abiliti o carichi le skill. [Guida alle skill Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Nuova barra laterale di Claude](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### Installazione locale con un comando

I comandi usano il ramo `main` di [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization). Funzioneranno dopo la pubblicazione del repository e del ramo. I link relativi agli ZIP funzionano anche in altri rami, tag e fork.

In una chat locale di Codex seleziona `$skill-installer` e invia la richiesta seguente. Autorizza la rete se richiesto, poi avvia una nuova sessione. [Guida alle skill Codex](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

La Skills CLI di terze parti installa la stessa cartella per Codex locale e Claude Code con un comando. Con Node.js 22.20 o successivo, eseguilo dal progetto di destinazione. Mantieni le opzioni `-a` degli agenti desiderati. Aggiungi `-g` per installare a livello utente. [Riferimento Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

Nella chat del terminale locale di Claude Code usa l’input della shell per installare solo per Claude. Verifica l’URL del repository prima di eseguire il comando. [Input della shell in Claude Code](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

In una nuova sessione richiama `$game-localization` in Codex o `/game-localization` in Claude Code. Per l’installazione manuale, copia tutta la cartella `game-localization/` in `.claude/skills/` nel progetto o in `~/.claude/skills/` per l’utente. [Guida alle skill Claude Code](https://code.claude.com/docs/en/skills)

Nelle versioni ospitate di ChatGPT e Claude usa i controlli di caricamento o installazione dell’account. Una menzione richiama la skill installata. Per un link condivisibile, pubblica tramite la directory della piattaforma o condividi la skill o il plugin in uno spazio idoneo. [Condividere plugin ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Condividere skill Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Usare la skill

1. Allega il testo o file sorgente e il glossario di progetto aggiornato per le lingue di destinazione. Se manca, chiedi esplicitamente una bozza.
2. Specifica lingue di partenza e arrivo, piattaforma, tipo di contenuto e formato di consegna. Aggiungi se pertinenti limiti di caratteri, schermate, note sui personaggi o esempi di variabili.
3. Per un foglio di calcolo indica le colonne di partenza e arrivo e chiedi una nuova copia. Per le stringhe del gioco fornisci ID o chiavi stabili. Per il negozio indica il campo e l’eventuale limite rigido.
4. Leggi il resoconto separato per sapere se il risultato è pronto per l’uso o è ancora una bozza. Il resoconto distingue il controllo del file, la revisione linguistica e la verifica nel gioco o nell’anteprima del negozio. Indica il passo successivo per ogni problema aperto. Approva i termini nel glossario del progetto prima di riutilizzarli.

Per l’interfaccia di gioco, il report di consegna include una lista di controlli in ordine di priorità, con schermata, ID della stringa, passaggi per riprodurre il caso e criterio di superamento. Si parte dai valori lunghi delle variabili e dai testi a rischio di taglio. Se sono noti il carattere e la larghezza utile, la skill può stimare lo spazio necessario. [Controlli in gioco](../game-localization/references/in-build-qa.md)

Usa il [modello di glossario del progetto](../game-localization/references/project-glossary-template.md) per tenere separati i termini approvati e le proposte. Salva il file aggiornato e allegalo alla prossima chat.

**Esempio per un foglio di calcolo**

~~~text
Usa Game Localization per tradurre in tedesco (de-DE) la colonna ENGLISH del file allegato. Scrivi le traduzioni in GERMAN in una nuova copia .xlsx. Usa il glossario allegato e la colonna DESCRIPTION come contesto. Conserva chiavi, colonne sorgente, segnaposto e tag. Elenca a parte domande terminologiche e verifiche con gli ID delle righe.
~~~

Per i file `.xlsx` supportati, indica il foglio, la riga di intestazione, la colonna con gli ID stabili, la colonna sorgente e la colonna di destinazione esistente. Con Python 3.9 o successivo, la skill scrive le traduzioni per ID in una nuova copia e verifica che il resto della cartella di lavoro sia preservato. Se la verifica non è possibile, può proporre un CSV con gli ID. [Istruzioni per Excel](../game-localization/references/xlsx-qa.md)

**Esempio per una pagina del negozio**

~~~text
Usa Game Localization per localizzare questa descrizione breve di Steam dall’inglese al portoghese brasiliano (pt-BR). Avvia una bozza del glossario se serve. Conserva il titolo del gioco e rispetta il limite di caratteri indicato. Restituisci il testo del negozio e un resoconto separato.
~~~

### Verificare le traduzioni CSV

Per un file CSV con ID di riga stabili, indica le intestazioni delle colonne con ID, testo sorgente e traduzione. Se è disponibile Python 3.9 o successivo, la skill confronta il file sorgente con quello tradotto e segnala ID mancanti o duplicati, traduzioni vuote, modifiche ai segnaposto o ai tag supportati e superamenti dei limiti di lunghezza. [Istruzioni per la verifica dei CSV](../game-localization/references/csv-qa.md)

Per aggiornare una traduzione, allega il CSV sorgente precedente e quello attuale, le traduzioni approvate e le modifiche editoriali successive. La skill abbina le righe per ID, conserva le traduzioni ancora adatte alle righe invariate e segnala quelle aggiunte, modificate e rimosse. Per i dialoghi lunghi, salva lo stato dopo ogni scena per riprendere con lo stesso file di lavoro. [Aggiornare le traduzioni CSV](../game-localization/references/csv-updates.md)

Prova [l’esempio introduttivo con 12 righe](../game-localization/examples/first-run/README.md). Include una bozza di traduzione, un glossario approvato e un resoconto di esempio.

### Le nostre impostazioni dei modelli

| Ambiente | Modello | Livello di ragionamento |
| --- | --- | --- |
| ChatGPT Work o Codex | GPT-6.1 Sol | High o superiore, se disponibile |
| Claude | Claude Opus 5.5 | High o superiore, se disponibile |

**High+** indica High o un livello superiore offerto dal client. Seleziona modello e livello nel client. La skill funziona indipendentemente da questa preferenza. [Modelli OpenAI](https://learn.chatgpt.com/docs/models) · [Livelli di ragionamento di Claude](https://platform.claude.com/docs/en/build-with-claude/effort)

## Aggiornare o rimuovere

| Installazione | Aggiornare | Rimuovere |
| --- | --- | --- |
| Plugin ChatGPT o Codex | Se gestisci il caricamento, usa **Upload new version** nella scheda del plugin. Le installazioni da directory o spazio ricevono aggiornamenti da quella fonte. | Apri **Plugins → Installed → Game Localization** e scegli **Uninstall plugin** se disponibile. Per un’installazione gestita, contatta l’amministratore. |
| Skill autonoma ChatGPT | Sostituisci il caricamento personale con lo ZIP autonomo più recente dalla gestione delle skill. | Apri **Plugins → Skills**, cercala in **Installed** o **Created by me** e usa l’opzione di rimozione se disponibile. Gli amministratori gestiscono le skill dello spazio. |
| Skill personalizzata Claude | Carica il nuovo ZIP autonomo dalla pagina di gestione. Disattiva la versione precedente se appare una seconda voce. | Apri la skill in **Customize → Skills** o **Plugins**, disattivala e per un tuo caricamento scegli **⋯ → Delete**. Conferma. |
| Skill locale installata con Skills CLI | Per un ramo tracciato esegui `npx skills update game-localization` o installa dal nuovo tag. | Esegui `npx skills remove game-localization` dallo stesso progetto. Aggiungi `-g` se l’installazione è globale. |
| Cartella locale o Codex Skill Installer | Sostituisci la cartella `game-localization/` con l’ultima versione. | Rimuovi `game-localization/`. Codex può caricarla da `.agents/skills/`, `~/.agents/skills/` o `~/.codex/skills/`. Claude Code usa `.claude/skills/` o `~/.claude/skills/`. Avvia una nuova sessione se serve. |

[Gestione dei plugin OpenAI](https://learn.chatgpt.com/docs/plugins) · [Gestione delle skill Claude personalizzate](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Sorgenti e pacchetti

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) definisce quando si attiva la skill e come elabora un lotto.
- [`game-localization/references/`](../game-localization/references/) contiene le regole e le versioni del glossario per lingua.
- [`packaging/chatgpt/`](../packaging/chatgpt/) contiene il manifest e l’icona del plugin.
- [`packages/`](../packages/) contiene gli archivi pronti da caricare.

Per ricreare i due ZIP, esegui `python scripts/package.py` dalla radice del repository con Python 3.9 o successivo. La versione viene dal manifest del plugin ChatGPT. Prima della distribuzione carica ogni ZIP nel prodotto previsto e prova un piccolo lotto con glossario e segnaposto protetto.

## Licenza

Game Localization è disponibile con [licenza MIT](../LICENSE). Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## Sostenere l’autore

Se Game Localization è utile al tuo team, puoi [sostenere Maled1kt su DonationAlerts](https://www.donationalerts.com/r/maled1kt). Le donazioni sono volontarie.
