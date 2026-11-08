# Game Localization

![Bannière Game Localization avec deux panneaux de dialogue qui échangent des caractères de plusieurs langues](../assets/game-localization-banner.png)

[English](../README.md) · [Toutes les langues](../README.md#languages)

Game Localization est une compétence d’agent pour traduire, réviser et contrôler les textes de jeux vidéo dans ChatGPT, Codex et Claude. Elle couvre les menus, tutoriels, dialogues, sous-titres, textes de boutique et documents de projet pour Steam, PlayStation, Xbox et les jeux mobiles.

[Installation](#installation) · [Utiliser la compétence](#utiliser-la-compétence) · [Mettre à jour ou supprimer](#mettre-à-jour-ou-supprimer) · [Soutenir l’auteur](#soutenir-lauteur)

## Fonctionnalités

- Applique la terminologie approuvée du projet et consigne les nouveaux termes comme propositions.
- Préserve les clés de localisation, les variables comme `{player_name}` et `%s`, les balises, les sauts de ligne significatifs et les autres éléments protégés.
- Vérifie les limites de longueur et sépare la traduction des questions, des corrections du texte source et des notes de contrôle qualité.
- Propose une [sélection de 30 langues et variantes](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages) et accepte des listes personnalisées.
- Comprend un [glossaire de départ de 75 termes dans les 30 langues et variantes](../game-localization/references/glossary/README.md), avec des définitions communes en anglais et des propositions de traduction.

La compétence contient des instructions et des références. Elle fonctionne sans clé API de projet, connecteur ni service en arrière-plan. La modification de fichiers dépend des outils du chat. Avant la sortie, vérifiez l’interface traduite dans le jeu et les textes de boutique dans l’aperçu de la plateforme.

## Installation

| Environnement | Paquet |
| --- | --- |
| ChatGPT ou Codex avec accès à l’import de plugins | [ZIP du plugin ChatGPT](../packages/game-localization-chatgpt-v0.1.3.zip) |
| Claude ou espace ChatGPT autorisant l’import de compétences autonomes | [ZIP de la compétence autonome](../packages/game-localization-skill-v0.1.3.zip) |
| Codex local ou Claude Code | [Installer depuis le dossier source](#installation-des-agents-locaux-en-une-commande) |

Sur GitHub, ouvrez le lien du paquet et choisissez **Download raw file**. Importez le ZIP sans le décompresser.

### ChatGPT et Codex

1. Dans ChatGPT sur le Web, ouvrez l’option d’import de plugins de votre compte. Les propriétaires et administrateurs autorisés peuvent utiliser **Admin console → Plugins → Add → Upload plugin**.
2. Sélectionnez le ZIP du plugin ChatGPT. Après validation, ouvrez **Game Localization** dans **Plugins** et choisissez **Install plugin** si proposé. Un import personnel peut apparaître sous **Personal → Created by me**.
3. Ouvrez un nouveau chat dans ChatGPT ou Codex. Saisissez `@` et sélectionnez **Game Localization**.

Si votre espace accepte les compétences autonomes, utilisez **Plugins → Skills → Create → Upload from your computer** pour importer le ZIP de la compétence. Attendez l’analyse et suivez les indications. Les options dépendent du compte et de l’espace. [Guide des plugins OpenAI](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Guide des compétences OpenAI](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. Activez **Code execution and file creation** dans Claude si votre compte ou espace l’exige.
2. Sur le Web ou dans Claude Desktop, ouvrez **Customize → Skills**. Dans la nouvelle interface, ouvrez **Plugins** dans la barre latérale et cherchez les commandes sous **Your plugins**.
3. Choisissez **+ → Create skill → Upload a skill** et sélectionnez le ZIP autonome. Activez `game-localization` dès qu’elle apparaît.
4. Ouvrez un nouveau chat et demandez à Claude d’utiliser **Game Localization**. Si la zone de saisie la propose sous **+** ou **/**, sélectionnez-la.

Dans un espace géré, un administrateur peut devoir activer ou importer les compétences. [Guide des compétences Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Nouvelle barre latérale Claude](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### Installation des agents locaux en une commande

Les commandes utilisent la branche `main` de [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization). Elles fonctionneront dès la publication du dépôt et de la branche. Les liens ZIP relatifs fonctionnent aussi sur d’autres branches, tags et forks.

Dans un chat Codex local, sélectionnez `$skill-installer` et envoyez la requête ci-dessous. Autorisez l’accès réseau si nécessaire, puis démarrez une nouvelle session. [Guide des compétences Codex](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

L’outil tiers Skills CLI installe le même dossier pour Codex local et Claude Code en une commande. Exécutez-la depuis le projet avec Node.js 22.20 ou ultérieur. Gardez les options `-a` des agents voulus et ajoutez `-g` pour une installation au niveau utilisateur. [Référence Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

Dans le chat du terminal local de Claude Code, utilisez la saisie shell pour installer la compétence pour Claude seul. Vérifiez l’URL du dépôt avant de lancer la commande. [Saisie shell dans Claude Code](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

Dans une nouvelle session, invoquez `$game-localization` dans Codex ou `/game-localization` dans Claude Code. Pour une installation manuelle, copiez tout le dossier `game-localization/` dans `.claude/skills/` du projet ou `~/.claude/skills/` pour votre compte. [Guide des compétences Claude Code](https://code.claude.com/docs/en/skills)

Dans ChatGPT et Claude hébergés, utilisez les commandes d’import ou d’installation du compte. Une mention appelle la compétence installée. Pour un lien partageable, publiez via le catalogue de la plateforme ou partagez la compétence ou le plugin dans un espace admissible. [Partager un plugin ChatGPT](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Partager une compétence Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Utiliser la compétence

1. Joignez le texte ou fichier source et le glossaire de projet pour les langues cibles. Sans glossaire, demandez explicitement une première version.
2. Précisez langues source et cibles, plateforme, type de contenu et format de sortie. Ajoutez au besoin limites de caractères, captures, notes sur les locuteurs ou exemples de variables.
3. Pour un classeur, indiquez les colonnes source et cible et demandez une nouvelle copie. Pour le jeu, fournissez des clés ou identifiants stables. Pour la boutique, indiquez le champ cible et la limite stricte éventuelle.
4. Dans le compte rendu, vérifiez les lignes en suspens, termes provisoires et contrôles effectués. Approuvez les termes avant de les réutiliser, puis vérifiez le texte dans le jeu ou l’aperçu de la boutique.

**Requête pour un classeur**

~~~text
Utilise Game Localization pour traduire en allemand (de-DE) la colonne ENGLISH du classeur joint. Écris les traductions dans GERMAN, dans une nouvelle copie .xlsx. Utilise le glossaire joint et la colonne DESCRIPTION comme contexte. Préserve les clés, colonnes source, variables et balises. Liste séparément les questions terminologiques et les contrôles avec les identifiants de ligne.
~~~

**Requête pour une page de boutique**

~~~text
Utilise Game Localization pour traduire cette description courte Steam de l’anglais vers le portugais du Brésil (pt-BR). Prépare un glossaire provisoire si nécessaire. Garde le titre du jeu et respecte la limite de caractères indiquée. Rends le texte et un compte rendu séparé.
~~~

### Nos réglages de modèles

| Environnement | Modèle | Niveau de raisonnement |
| --- | --- | --- |
| ChatGPT Work ou Codex | GPT-6.1 Sol | High ou supérieur, selon disponibilité |
| Claude | Claude Opus 5.5 | High ou supérieur, selon disponibilité |

**High+** désigne High ou un niveau supérieur disponible dans le client. Choisissez-y le modèle et le niveau. La compétence fonctionne indépendamment de ce réglage. [Réglages des modèles OpenAI](https://learn.chatgpt.com/docs/models) · [Niveaux de raisonnement de Claude](https://platform.claude.com/docs/en/build-with-claude/effort)

## Mettre à jour ou supprimer

| Installation | Mettre à jour | Supprimer |
| --- | --- | --- |
| Plugin ChatGPT ou Codex | Si vous gérez l’import, choisissez **Upload new version** dans les détails du plugin. Les installations de catalogue ou d’espace reçoivent leurs mises à jour de cette source. | Ouvrez **Plugins → Installed → Game Localization** et choisissez **Uninstall plugin** si proposé. Pour une installation gérée, contactez l’administrateur. |
| Compétence autonome ChatGPT | Remplacez votre import personnel par le ZIP autonome le plus récent depuis la gestion des compétences. | Dans **Plugins → Skills**, trouvez-la sous **Installed** ou **Created by me** et choisissez l’option de suppression si disponible. Les administrateurs gèrent les compétences de l’espace. |
| Compétence personnalisée Claude | Importez le nouveau ZIP autonome depuis la page de gestion. Désactivez l’ancienne version si l’import crée une deuxième entrée. | Ouvrez-la sous **Customize → Skills** ou **Plugins**, désactivez-la et choisissez **⋯ → Delete** pour votre propre import. Confirmez. |
| Compétence locale installée avec Skills CLI | Pour une branche suivie, exécutez `npx skills update game-localization` ou installez depuis le nouveau tag. | Exécutez `npx skills remove game-localization` dans le même projet. Ajoutez `-g` si l’installation était globale. |
| Dossier local ou Codex Skill Installer | Remplacez le dossier `game-localization/` par la dernière version. | Supprimez `game-localization/`. Codex peut le charger depuis `.agents/skills/`, `~/.agents/skills/` ou `~/.codex/skills/`. Claude Code utilise `.claude/skills/` ou `~/.claude/skills/`. Ouvrez une nouvelle session si nécessaire. |

[Gestion des plugins OpenAI](https://learn.chatgpt.com/docs/plugins) · [Gestion des compétences personnalisées Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Sources et empaquetage

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) définit quand la compétence intervient et comment elle traite un lot.
- [`game-localization/references/`](../game-localization/references/) contient les règles et les versions du glossaire de départ.
- [`packaging/chatgpt/`](../packaging/chatgpt/) contient le manifeste et l’icône du plugin.
- [`packages/`](../packages/) contient les archives prêtes à importer.

Pour reconstruire les deux ZIP, exécutez `python scripts/package.py` à la racine du dépôt avec Python 3.9 ou ultérieur. Le numéro de version vient du manifeste du plugin ChatGPT. Avant diffusion, importez chaque ZIP dans le produit prévu et testez un petit lot avec un glossaire et une variable protégée.

## Licence

Game Localization est disponible sous [licence MIT](../LICENSE). Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## Soutenir l’auteur

Si Game Localization aide votre équipe, vous pouvez [soutenir Maled1kt via DonationAlerts](https://www.donationalerts.com/r/maled1kt). Les dons sont entièrement facultatifs.
