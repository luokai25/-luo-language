#!/usr/bin/env python3
"""Validate stable IDs and safety metadata in the Luo glyph asset manifest."""
from __future__ import annotations
import json
import sys
from pathlib import Path

MANIFEST = Path(__file__).resolve().parents[1] / "glyphs" / "manifest.json"
EXPECTED = [f"LUO-{n:03d}" for n in range(1, 31)]

def main() -> int:
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read glyph manifest: {exc}", file=sys.stderr)
        return 2
    glyphs = data.get("glyphs", [])
    ids = [item.get("id") for item in glyphs]
    if ids != EXPECTED:
        print("ERROR: glyph IDs must be LUO-001 through LUO-030 exactly once and in order.")
        print(f"Found: {ids}")
        return 1
    paths = [item.get("crop_file") for item in glyphs]
    if len(set(paths)) != 30 or any(not path for path in paths):
        print("ERROR: every glyph must have a unique crop path.")
        return 1
    if any(item.get("creator_approved") is not False for item in glyphs):
        print("ERROR: unreviewed source crops must not be marked creator-approved.")
        return 1
    if any(item.get("vector_master") is not None for item in glyphs):
        print("ERROR: vector masters cannot be declared before review.")
        return 1
    print("OK: 30 glyph records are unique, ordered, and correctly marked provisional.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
