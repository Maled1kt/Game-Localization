"""Estimate the horizontal space needed by one already-formatted UI label."""

import argparse
import json
import math
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--font", type=Path, required=True, help="Exact .ttf or .otf font file")
    parser.add_argument("--font-size-px", type=int, required=True, help="Effective font size after UI scaling")
    parser.add_argument("--usable-width-px", type=float, required=True, help="Width left after padding and icons")
    parser.add_argument("--text", required=True, help="Plain single-line text with all variables filled in")
    parser.add_argument("--direction", choices=("ltr", "rtl"), required=True)
    parser.add_argument("--language", help="BCP 47 language tag for text shaping")
    args = parser.parse_args()
    if (args.font_size_px <= 0 or not math.isfinite(args.usable_width_px)
            or args.usable_width_px <= 0):
        parser.error("Font size and usable width must be finite and positive.")
    if not args.text.strip() or args.text.splitlines() != [args.text] or "\t" in args.text:
        parser.error("Supply nonblank, single-line display text without tabs.")
    if args.font.suffix.lower() not in (".ttf", ".otf") or not args.font.is_file():
        parser.error("Supply an existing .ttf or .otf font file.")

    try:
        from PIL import ImageFont, features

        shaped = features.check_feature("raqm")
        if not shaped and (args.direction != "ltr" or not all(
            " " <= char <= "~" or "\u00a0" <= char <= "\u00ff" for char in args.text
        )):
            parser.error("This text requires Pillow with Raqm. Basic layout supports only Latin-1 left-to-right text.")
        layout = ImageFont.Layout.RAQM if shaped else ImageFont.Layout.BASIC
        with args.font.open("rb") as file:
            font = ImageFont.truetype(file, args.font_size_px, layout_engine=layout)
        shaping = {"direction": args.direction, "language": args.language} if shaped else {}
        advance = font.getlength(args.text, **shaping)
        left, _, right, _ = font.getbbox(args.text, **shaping)
    except (ImportError, AttributeError):
        parser.error("Width estimation requires Pillow 9.2 or later.")
    except (OSError, ValueError, OverflowError) as error:
        parser.error(f"Could not estimate text width: {error}")

    required = math.ceil(max(advance, right) - min(0, left))
    print(json.dumps({
        "method": "Pillow with Raqm" if shaped else "Pillow basic layout",
        "estimated_width_px": required,
        "usable_width_px": args.usable_width_px,
        "remaining_width_px": args.usable_width_px - required,
        "overflow_risk": required > args.usable_width_px,
    }))


if __name__ == "__main__":
    main()
