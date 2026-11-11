import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class GlyphManifestTests(unittest.TestCase):
    def test_glyph_manifest_validator_passes(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "validate_glyph_manifest.py")],
            check=False, capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("30 glyph records", result.stdout)

if __name__ == "__main__":
    unittest.main()
