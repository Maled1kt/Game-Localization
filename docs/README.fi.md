# Game Localization

![Game Localization -bannerissa kaksi pelin keskusteluruutua vaihtaa eri kielten merkkejä](../assets/game-localization-banner.png)

[English](../README.md) · [Kaikki kielet](../README.md#languages)

Game Localization on agenttitaito pelitekstien kääntämiseen, muokkaamiseen ja tarkistamiseen ChatGPT:ssä, Codexissa ja Claudessa. Sillä voi käsitellä valikoita, opastuksia, dialogia, tekstityksiä, kauppatekstejä ja projektiasiakirjoja Steamille, PlayStationille, Xboxille ja mobiilipeleille.

[Asennus](#asennus) · [Taidon käyttäminen](#taidon-käyttäminen) · [Päivittäminen tai poistaminen](#päivittäminen-tai-poistaminen) · [Tue tekijää](#tue-tekijää)

## Ominaisuudet

- Soveltaa projektissa hyväksyttyä sanastoa ja kirjaa uudet termit ehdotuksiksi.
- Säilyttää lokalisointiavaimet, paikkamerkit kuten `{player_name}` ja `%s`, tunnisteet, merkitykselliset rivinvaihdot ja muut suojatut osat.
- Tarkistaa annetut pituusrajat ja pitää käännökset erillään kysymyksistä, lähdetekstin korjauksista ja laaduntarkistuksen huomioista.
- Tarjoaa [30 kielen ja kielivariantin oletusluettelon](../game-localization/references/game-localization-rules-v0.1.md#21-select-target-languages) sekä tuen omille luetteloille.
- Sisältää [75 termin aloitussanaston kaikille 30 kielelle ja variantille](../game-localization/references/glossary/README.md). Yhteiset määritelmät ovat englanniksi, ja käännökset ovat ehdotuksia.

Taito sisältää ohjeet ja viitetiedostot. Se toimii ilman projektin API-avainta, liitintä tai taustapalvelua. Tiedostojen muokkaus riippuu keskustelun työkaluista. Tarkista ennen julkaisua käännetty käyttöliittymä pelin koontiversiossa ja kauppateksti alustan esikatselussa.

## Asennus

| Ympäristö | Paketti |
| --- | --- |
| ChatGPT tai Codex, jossa on lupa ladata laajennuksia | [ChatGPT-laajennuksen ZIP](../packages/game-localization-chatgpt-v0.1.3.zip) |
| Claude tai ChatGPT-työtila, joka sallii erillisten taitojen lataamisen | [Erillisen taidon ZIP](../packages/game-localization-skill-v0.1.3.zip) |
| Paikallinen Codex tai Claude Code | [Asenna lähdekansiosta](#asennus-paikallisille-agenteille-yhdellä-komennolla) |

Avaa pakettilinkki GitHubissa ja valitse **Download raw file**. Lataa ZIP purkamatta sitä.

### ChatGPT ja Codex

1. Avaa tilisi laajennusten lataustoiminto ChatGPT:n verkkoversiossa. Oikeutetut omistajat ja ylläpitäjät voivat käyttää polkua **Admin console → Plugins → Add → Upload plugin**.
2. Valitse laajennuksen ZIP. Avaa tarkistuksen jälkeen **Game Localization** kohdasta **Plugins** ja valitse **Install plugin**, jos se on tarjolla. Henkilökohtainen lataus voi näkyä kohdassa **Personal → Created by me**.
3. Aloita uusi keskustelu ChatGPT:ssä tai Codexissa. Kirjoita `@` ja valitse ehdotuksista **Game Localization**.

Jos työtila tukee erillisiä taitoja, lataa taidon ZIP kohdassa **Plugins → Skills → Create → Upload from your computer**. Odota tarkistusta ja noudata ohjeita. Valinnat riippuvat tilistä ja työtilasta. [OpenAI-laajennusten ohje](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [OpenAI-taitojen ohje](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Claude

1. Ota Claude-asetuksissa käyttöön **Code execution and file creation**, jos tili tai työtila sitä edellyttää.
2. Avaa **Customize → Skills** Claude-verkkopalvelussa tai Claude Desktopissa. Uudessa näkymässä avaa sivupalkin **Plugins** ja etsi hallinta kohdasta **Your plugins**.
3. Valitse **+ → Create skill → Upload a skill** ja erillinen ZIP. Ota `game-localization` käyttöön, kun se tulee näkyviin.
4. Aloita uusi keskustelu ja pyydä Claudea käyttämään **Game Localization** -taitoa. Jos taito löytyy syöttökentän **+**- tai **/**-valikosta, valitse se sieltä.

Hallinnoidussa työtilassa ylläpitäjän on ehkä otettava taidot käyttöön tai ladattava ne. [Claude-taitojen ohje](https://support.claude.com/en/articles/12512180-use-skills-in-claude) · [Clauden uusi sivupalkki](https://support.claude.com/en/articles/17740565-manage-plugins-skills-and-connectors-from-one-plugins-page)

### Asennus paikallisille agenteille yhdellä komennolla

Komennot käyttävät [Maled1kt/game-localization](https://github.com/Maled1kt/game-localization) -tietovaraston `main`-haaraa. Ne toimivat, kun tietovarasto ja haara on julkaistu. Suhteelliset ZIP-linkit toimivat muissakin haaroissa, tunnisteissa ja haarautetuissa kopioissa.

Valitse paikallisessa Codex-keskustelussa `$skill-installer` ja lähetä alla oleva pyyntö. Salli verkkoyhteys pyydettäessä ja aloita uusi istunto. [Codex-taitojen ohje](https://learn.chatgpt.com/docs/build-skills)

~~~text
$skill-installer Install the skill from https://github.com/Maled1kt/game-localization/tree/main/game-localization
~~~

Kolmannen osapuolen Skills CLI asentaa saman lähdekansion paikalliseen Codexiin ja Claude Codeen yhdellä komennolla. Suorita komento kohdeprojektissa Node.js 22.20:llä tai uudemmalla. Säilytä tarvittavien agenttien `-a`-valinnat. Lisää `-g` käyttäjäkohtaiseen asennukseen. [Skills CLI -ohje](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add)

~~~bash
npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a codex -a claude-code
~~~

Asenna taito vain Claudeen käyttämällä paikallisen Claude Coden päätekeskustelun komentotulkkisyötettä. Tarkista tietovaraston URL ennen komentoa. [Claude Coden komentotulkkisyöte](https://code.claude.com/docs/en/interactive-mode#shell-mode-with--prefix)

~~~text
! npx skills add https://github.com/Maled1kt/game-localization/tree/main/game-localization -a claude-code
~~~

Kutsu uudessa istunnossa Codexissa `$game-localization` tai Claude Codessa `/game-localization`. Manuaalista asennusta varten kopioi koko `game-localization/`-kansio projektin `.claude/skills/`-kansioon tai käyttäjän `~/.claude/skills/`-kansioon. [Claude Coden taito-ohje](https://code.claude.com/docs/en/skills)

Käytä ChatGPT:n ja Clauden verkkopalveluissa tilisi lataus- tai asennustoimintoa. Maininta kutsuu asennettua taitoa. Jaettavan linkin saat julkaisemalla alustan tukemassa hakemistossa tai jakamalla taidon tai laajennuksen siihen oikeutetussa työtilassa. [ChatGPT-laajennusten jakaminen](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt) · [Claude-taitojen jakaminen](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Taidon käyttäminen

1. Liitä lähdeteksti tai tiedosto ja kohdekielten ajantasainen projektisanasto. Jos sanastoa ei ole, pyydä nimenomaisesti luonnosta.
2. Määritä lähde- ja kohdekielet, alusta, aineiston tyyppi ja tulostusmuoto. Lisää tarvittaessa merkkirajat, kuvakaappaukset, puhujatiedot tai muuttujien esimerkit.
3. Nimeä laskentataulukon lähde- ja kohdesarakkeet ja pyydä uutta kopiota. Anna peliteksteille pysyvät tunnukset tai avaimet. Ilmoita kauppatekstin kohdekenttä ja mahdollinen tiukka pituusraja.
4. Tarkista luovutusraportista avoimet rivit, alustavat termit ja tehdyt tarkistukset. Hyväksy termit projektisanastossa ennen uudelleenkäyttöä ja tarkista teksti peliversiossa tai kaupan esikatselussa.

**Kehote-esimerkki laskentataulukolle**

~~~text
Käännä Game Localizationilla liitetyn työkirjan ENGLISH-sarake saksaksi (de-DE). Kirjoita käännökset uuden .xlsx-kopion GERMAN-sarakkeeseen. Käytä liitettyä sanastoa ja DESCRIPTION-saraketta taustatietoina. Säilytä avaimet, lähdesarakkeet, paikkamerkit ja tunnisteet. Listaa termikysymykset ja tarkistukset erikseen rivitunnuksineen.
~~~

**Kehote-esimerkki kauppasivulle**

~~~text
Lokalisoi Game Localizationilla tämä Steamin lyhyt kuvaus englannista brasilianportugaliksi (pt-BR). Laadi tarvittaessa sanastoluonnos. Säilytä pelin nimi ja noudata annettua merkkirajaa. Palauta kauppateksti ja erillinen luovutusraportti.
~~~

### Käyttämämme malliasetukset

| Ympäristö | Malli | Päättelyn taso |
| --- | --- | --- |
| ChatGPT Work tai Codex | GPT-6.1 Sol | High tai korkeampi, jos saatavilla |
| Claude | Claude Opus 5.5 | High tai korkeampi, jos saatavilla |

**High+** tarkoittaa asiakassovelluksen High-tasoa tai sitä korkeampaa tasoa. Valitse malli ja taso sovelluksessa. Taito toimii asetuksesta riippumatta. [OpenAI:n malliasetukset](https://learn.chatgpt.com/docs/models) · [Clauden päättelytasot](https://platform.claude.com/docs/en/build-with-claude/effort)

## Päivittäminen tai poistaminen

| Asennustapa | Päivitä | Poista |
| --- | --- | --- |
| ChatGPT- tai Codex-laajennus | Jos hallitset latausta, valitse laajennuksen tiedoista **Upload new version**. Hakemistosta tai työtilasta asennettu laajennus päivittyy samasta lähteestä. | Avaa **Plugins → Installed → Game Localization** ja valitse **Uninstall plugin**, jos tarjolla. Kysy hallinnoidusta asennuksesta ylläpitäjältä. |
| Erillinen ChatGPT-taito | Korvaa henkilökohtainen lataus uusimmalla erillisellä ZIPillä taidon hallinnassa. | Avaa **Plugins → Skills**, etsi taito kohdasta **Installed** tai **Created by me** ja käytä poistotoimintoa. Ylläpitäjä hallitsee työtilan taitoja. |
| Mukautettu Claude-taito | Lataa uusi erillinen ZIP hallintasivulta. Poista aiempi versio käytöstä, jos syntyy toinen merkintä. | Avaa taito kohdassa **Customize → Skills** tai **Plugins** ja poista se käytöstä. Valitse omalle latauksellesi **⋯ → Delete** ja vahvista. |
| Skills CLI:llä asennettu paikallinen taito | Suorita seuratulle haaralle `npx skills update game-localization` tai asenna uudesta tunnisteesta. | Suorita samassa projektissa `npx skills remove game-localization`. Lisää `-g`, jos asensit taidon globaalisti. |
| Paikallinen kansio tai Codex Skill Installer | Korvaa asennettu `game-localization/`-kansio uusimmalla versiolla. | Poista `game-localization/`. Codex voi ladata sen kansioista `.agents/skills/`, `~/.agents/skills/` tai `~/.codex/skills/`. Claude Code käyttää kansioita `.claude/skills/` tai `~/.claude/skills/`. Aloita tarvittaessa uusi istunto. |

[OpenAI-laajennusten hallinta](https://learn.chatgpt.com/docs/plugins) · [Mukautettujen Claude-taitojen hallinta](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

## Lähdekoodi ja paketointi

- [`game-localization/SKILL.md`](../game-localization/SKILL.md) määrittää, milloin taito käynnistyy ja miten se käsittelee tekstierän.
- [`game-localization/references/`](../game-localization/references/) sisältää säännöt ja kielikohtaiset aloitussanastot.
- [`packaging/chatgpt/`](../packaging/chatgpt/) sisältää laajennuksen manifestin ja kuvakkeen.
- [`packages/`](../packages/) sisältää latausvalmiit paketit.

Luo molemmat ZIPit samasta lähteestä suorittamalla `python scripts/package.py` tietovaraston juurikansiossa Python 3.9:llä tai uudemmalla. Versio saadaan ChatGPT-laajennuksen manifestista. Lataa kumpikin ZIP kohdetuotteeseen ennen jakelua ja testaa pientä tekstierää, jossa on sanasto ja suojattu paikkamerkki.

## Lisenssi

Game Localization on saatavana [MIT-lisenssillä](../LICENSE). Copyright (c) 2026 [Maled1kt](https://github.com/Maled1kt).

## Tue tekijää

Jos Game Localization auttaa tiimiäsi, voit [tukea Maled1ktiä DonationAlertsissa](https://www.donationalerts.com/r/maled1kt). Lahjoittaminen on vapaaehtoista.
