#!/usr/bin/env python3
"""Extract provisional Luo glyph reference crops from the creator's 3x10 sheet.

The source image is never modified. Coordinates are explicit and may need review
when a different photograph, crop, or camera angle is used.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw

# Coordinates for the clearer reference photograph at 4624x3472.
# Each tuple is (center_x, center_y, half_width, half_height).
TOP_X = [480 + 400 * i for i in range(10)]
MIDDLE_X = TOP_X[:]
BOXES = [
    [(x, 520, 190, 180) for x in TOP_X],
    [(x, 920, 190, 185) for x in MIDDLE_X],
    [
        (400, 1400, 350, 250),
        (980, 1400, 180, 250),
        (1380, 1400, 180, 250),
        (1830, 1400, 180, 250),
        (2110, 1400, 180, 250),
        (2500, 1400, 165, 250),
        (2900, 1400, 165, 250),
        (3260, 1400, 175, 250),
        (3680, 1400, 180, 250),
        (4200, 1400, 170, 250),
    ],
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="creator-supplied reference photograph")
    parser.add_argument("--out", type=Path, default=Path("glyphs"))
    args = parser.parse_args()

    source = Image.open(args.source).convert("RGB")
    args.out.mkdir(parents=True, exist_ok=True)
    crop_dir = args.out / "source-crops"
    crop_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "schema": "luo-glyph-assets/0.1",
        "status": "provisional-source-crops",
        "source_file": args.source.name,
        "source_dimensions": list(source.size),
        "reading_order": "three rows, left to right",
        "approval": "not yet creator-approved as isolated crops or vector masters",
        "glyphs": [],
    }
    contact = Image.new("RGB", (1050, 1140), "white")
    draw = ImageDraw.Draw(contact)

    index = 0
    for row in BOXES:
        for cx, cy, half_w, half_h in row:
            index += 1
            bounds = [
                max(0, cx - half_w),
                max(0, cy - half_h),
                min(source.width, cx + half_w),
                min(source.height, cy + half_h),
            ]
            crop = source.crop(tuple(bounds))
            filename = f"LUO-{index:03d}.jpg"
            crop.save(crop_dir / filename, quality=96, optimize=True)

            thumb = crop.copy()
            thumb.thumbnail((180, 150))
            col, row_index = (index - 1) % 5, (index - 1) // 5
            px, py = col * 210 + 15, row_index * 190 + 25
            contact.paste(thumb, (px, py))
            draw.text((px, py - 18), f"LUO-{index:03d}", fill="black")

            manifest["glyphs"].append({
                "id": f"LUO-{index:03d}",
                "row": (index - 1) // 10 + 1,
                "column": (index - 1) % 10 + 1,
                "crop_file": f"source-crops/{filename}",
                "source_bounds_xyxy": bounds,
                "vector_master": None,
                "creator_approved": False,
            })

    contact.save(args.out / "contact-sheet.jpg", quality=94, optimize=True)
    (args.out / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Extracted {index} provisional crops into {args.out}")


if __name__ == "__main__":
    main()
