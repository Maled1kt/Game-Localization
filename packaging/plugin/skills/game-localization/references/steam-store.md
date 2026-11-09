# Localize a Steam store page

Use this workflow for the written description on a Steam store page. Work on one target locale at a time. Return the short description and About This Game as separate fields and put checks in the handoff.

## Get the source and confirmed facts

Ask for the two source fields or a Steamworks store localization export, the target locale, the approved title and terminology, and the field limits shown in the editor or supplied in the brief. Confirm the exact language key in any export. The store page language and the languages supported inside the game are separate settings. [Steamworks localization documentation](https://partner.steamgames.com/doc/store/localization)

Read the source and the latest approved project notes for features, player counts, modes, platforms, edition contents, release status, awards, and language support. Before handoff, trace each material claim to that evidence and compare the translation with it. Preserve qualifications such as local play, up to two players, or a planned feature. Flag contradictions by field and ask for a decision before treating that field as final. [Steamworks review process](https://partner.steamgames.com/doc/store/Review_Process)

## Write and check each field

| Field | Translation and QA |
| --- | --- |
| Short description | Write a concise plain-text synopsis on one line. Keep the core hook and key facts within the supplied limit. Avoid dated announcements and formatting. |
| About This Game | Preserve the intended order, headings, lists, and protected markup. Translate visible prose and preserve embedded asset references. Keep detailed claims and edition differences grounded in the brief. |

Valve describes a short plain-text synopsis and a longer formatted description. It also sets restrictions on promotional links and references to other products. Review those restrictions before handoff and use the dedicated Steamworks fields for applicable links, reviews, and awards. [Steamworks written description guidance](https://partner.steamgames.com/doc/store/page/description)

Report the length of each final field and the applied limit and unit. If a required limit or its counting rule is unknown, give the local count and mark the limit check pending until someone confirms it in the editor. Keep local file checks, fact and language review, Steamworks import, and store preview separate.

## Prepare a JSON draft when an export is supplied

The [draft helper](../scripts/prepare_steam_store.py) supports multilingual UTF-8 JSON exports with an `itemid`, a `languages` object, and existing source and target language objects. It maps `short_description` and `about` to their matching Steamworks fields. It preserves the other JSON values, including other languages and unrelated fields. The helper uses Python 3.9 or later and the standard library. [Crowdin's format example](https://store.crowdin.com/steam-json)

Save the reviewed text in a separate JSON object with `short_description`, `about`, or both. Run from the skill folder and choose a new output path.

```sh
python -B scripts/prepare_steam_store.py store-export.json reviewed.de-DE.json store.de-DE.draft.json --source-language english --target-language german --short-limit 90
```

The example limit of 90 is a fictional project limit. Supply the confirmed limit for the actual field with `--short-limit` or `--about-limit`, measured in Unicode code points. The report also gives UTF-8 byte counts. For another counting rule, verify it separately in the agreed unit. Without a supplied limit, the helper reports that field's length check as pending.

The helper rejects over-limit fields, blank text, formatting in the short description, and changes to supported BBCode, image or link targets, or protected tokens. For approved localized images or deliberate layout differences, review those changes in the Steamworks editor. Use `--replace-existing` only for a confirmed replacement of populated target text in the new draft. The original export stays available as a reference. If the export shape differs or the target language is absent, return the field copy separately for entry through the editor's language selector. [Steamworks language selector](https://partner.steamgames.com/doc/store/localization)

## Verify a trial import and preview

1. Use a designated Steamworks draft or test page and confirm that the export's item ID and target language match. Save a fresh export of the current draft before testing. For a trial with the same wording, compare the candidate with that export first so an older snapshot cannot overwrite newer edits.
2. In the store page editor's **Localization** tab, import the candidate JSON into the draft and record the result. Confirm that the expected fields and language are present. Re-export and compare the relevant values if available. Valve documents import and export from this tab for store localization text. [Steamworks asset and accessibility text guidance](https://partner.steamgames.com/doc/store/page/assets)
3. Open **Preview changes in store** and select the target language. Check that the short description appears in full, headings and lists render, embedded assets load, and the copy matches the reviewed text. Leave the changes in draft for review. [Steamworks store beta mode](https://partner.steamgames.com/doc/store/page)

If the portal is unavailable, hand off the draft or field copy and mark import and preview as pending. A local JSON check establishes which values changed. Steamworks acceptance requires a trial import.

## Fictional example

The source describes a repair game named Signal Station with solo play and local co-op for two players. The approved brief confirms those modes and the title. A translation that advertises online co-op or four players needs a fact correction.

**`store-export.json`**

```json
{
  "itemid": "0",
  "languages": {
    "english": {
      "app[content][short_description]": "Repair a space station solo or in local co-op for two.",
      "app[content][about]": "[h2]Signal Station[/h2]\nRestore power solo or with a second player in local co-op.\n[img]{STEAM_APP_IMAGE}/extras/repair.png[/img]"
    },
    "german": {
      "app[content][short_description]": "",
      "app[content][about]": ""
    }
  }
}
```

**`reviewed.de-DE.json`**

```json
{
  "short_description": "Repariere eine Raumstation allein oder zu zweit im lokalen Koop.",
  "about": "[h2]Signal Station[/h2]\nStelle die Stromversorgung allein oder zu zweit im lokalen Koop wieder her.\n[img]{STEAM_APP_IMAGE}/extras/repair.png[/img]"
}
```

Use this fictional example locally. The expected handoff records the short description's length against the supplied 90-character limit, the preserved title and image reference, and the solo and local two-player claims. The example leaves import and preview pending.
