# In-build localization checks

For UI strings that warrant a layout check, put a short, prioritized checklist in the handoff. Use one row per distinct scenario. Start with long variable values in narrow or fixed-width elements, then check static labels likely to clip. Give priority to cases where hidden text changes what a player can do or understand. Apply only platform, viewport, scale, and input combinations the project supports.

## Write a check someone can reproduce

1. Name the screen or scene, the element, and the source ID. Use the resource key or another supplied locator if there is no ID. If a screen or trigger is unknown, flag the missing detail by ID and keep the check pending.
2. Specify the locale and the steps to reach the element. Include relevant conditions such as the narrowest supported viewport, highest supported text scale, or input device. For a variable, supply the exact test value and the resulting display text. Use permitted long values, including formatted numbers or multi-part input labels where applicable. Mark proposed values as test candidates if the project has yet to confirm them.
3. Give an observable pass condition. Check that the expected substitution appears and that essential text is legible without clipping or overlap. Use the project's rules for wrapping, ellipsis, and input icons. Keep the case pending until that scenario is inspected. Record the build or preview, conditions, and observed result if evidence is available. Scope screenshot evidence to the visible case.

## Estimate single-line width when the inputs are available

- Use the project's renderer or text measurements first. Compare the fully substituted text's width with the space available to text at the same scale. Subtract padding, icons, and gaps from the element width if they occupy that space. For example, a 248 px label with 220 px available exceeds the budget by 28 px.
- For plain, single-line text in one font, use the [optional width estimator](../scripts/estimate_ui_width.py) when the exact font file, effective size, text direction, and usable width are known and the font covers the text. Run it from the skill folder with Python and Pillow 9.2 or later. Pass the text as it will appear, after substitutions and display transformations. Use `--language` when the locale is known. Raqm enables language-specific shaping and right-to-left text. Without it the helper estimates only left-to-right Latin-1 text with basic layout. Use the game renderer if the label requires language-specific shaping.

```sh
python scripts/estimate_ui_width.py --font "ui.ttf" --font-size-px 18 --usable-width-px 220 --direction ltr --language de-DE --text "Halte Umschalt + Eingabe gedrückt, um die Luftschleuse zu öffnen"
```

- Record the method, estimated width, available width, and overage or remaining room. The helper rounds up a width that includes both text advance and glyph overhang. Treat a width over budget as a priority for inspection. Even an estimate within budget leaves the in-build check pending. [Pillow font measurements](https://pillow.readthedocs.io/en/stable/reference/ImageFont.html)
- If the label uses rich text, font fallback, embedded icons, wrapping, or engine-specific spacing and scaling that the helper cannot represent, use a measurement from the game or leave the estimate unavailable. When any required input or tool is missing, name it and keep the manual check. Character counts are useful for file limits and give no width measurement.

## Example checklist

These fictional scenarios use the [German first-run example](../examples/first-run/README.md). The example assumes the stated test binding is supported. The build and layout measurements are unavailable.

| Status | Screen and ID | Reproduce | Pass when |
| --- | --- | --- | --- |
| Pending | Docking area, airlock prompt `TUT_014` | Set the locale to `de-DE`, bind Interact to `Umschalt + Eingabe`, and approach the closed airlock at the highest supported text scale. | The complete prompt `Halte Umschalt + Eingabe gedrückt, um die Luftschleuse zu öffnen` is visible without clipping or overlap. |
| Pending | Tutorial next-step button `MENU_005` | Set the locale to `de-DE`, reach the next-step button in the tutorial, and use the narrowest supported viewport. | `Weiter` is visible in full inside the button. |
