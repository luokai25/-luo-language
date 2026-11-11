#!/usr/bin/env python3
"""Validate Luo's 30-entry character register.

This checks IDs and register completeness only. It does not draw glyphs,
assign meanings, or claim that digital font assets exist.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REGISTER = Path(__file__).resolve().parents[1] / "spec" / "CHARACTER-REGISTER.md"
EXPECTED_IDS = [f"LUO-{number:03d}" for number in range(1, 31)]


def main() -> int:
    if not REGISTER.is_file():
        print(f"ERROR: register not found: {REGISTER}", file=sys.stderr)
        return 2

    content = REGISTER.read_text(encoding="utf-8")
    found = re.findall(r"\|\s*(LUO-\d{3})\s*\|", content)

    if found != EXPECTED_IDS:
        print("ERROR: character register is incomplete, duplicated, or out of order.")
        print(f"Expected: {', '.join(EXPECTED_IDS)}")
        print(f"Found:    {', '.join(found)}")
        return 1

    print("OK: all 30 Luo character IDs are present exactly once and in order.")
    print("Note: this validates the textual register, not glyph artwork.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
