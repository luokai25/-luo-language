import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class CharacterRegisterTests(unittest.TestCase):
    def test_register_validator_passes(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "validate_character_register.py")],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("all 30 Luo character IDs", result.stdout)


if __name__ == "__main__":
    unittest.main()
