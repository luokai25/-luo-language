# Luo Glyph Asset Pipeline

## Authority and preservation

The creator-supplied handwritten reference sheet is the sole visual authority for LUO-001 through LUO-030. The inventory order is three rows of ten, read left to right. LUO-030 is the bold crossed X and is intentional.

Never redraw a glyph from its prose description, substitute a familiar symbol, or silently normalize its stroke shape. Keep source photographs unchanged. Crops and future vector masters are derivatives and must retain a link to their source image and character ID.

## Current digitization stage

The current working session has two photographs of the same handwritten sheet. The second photograph is used for the initial crop geometry because it is clearer. The extraction tool creates numbered source crops and a contact sheet. These are reference crops, not approved font outlines.

No pronunciation, meaning, translation, or syntax role is assigned by this pipeline. No character encoding is approved here.

## Reproducible extraction

Run:

```bash
python -m pip install pillow
python tools/extract_glyphs.py path/to/reference-photo.jpg --out glyphs
```

The tool writes:
- `glyphs/source-crops/LUO-001.jpg` through `LUO-030.jpg`
- `glyphs/contact-sheet.jpg`
- `glyphs/manifest.json`

The source photo is not modified. Crop coordinates are explicit and version-controlled so corrections can be reviewed rather than hidden in an image editor.

## Approval gates before font production

1. Review every crop against the full original photograph.
2. Correct crop bounds where a neighboring glyph or ruled line intrudes.
3. Obtain creator approval for all 30 isolated source crops.
4. Trace editable vector masters without changing stroke geometry.
5. Compare each vector overlay against the photograph at high zoom.
6. Obtain creator approval for the vector set before using it in a font.
7. Add rendering, typing, serialization, and round-trip tests.

A vector that merely looks similar is not a faithful master. Keep the source photograph available for every review.
