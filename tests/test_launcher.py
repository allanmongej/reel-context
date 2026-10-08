"""The public launcher must work outside the project's working directory."""

import os
import subprocess
import tempfile
import unittest
from pathlib import Path


@unittest.skipUnless(os.name == "posix", "The shell launcher targets macOS/Linux.")
class LauncherTest(unittest.TestCase):
    def test_named_launcher_works_from_another_directory(self):
        launcher = Path(__file__).resolve().parents[1] / "bin" / "reel-context"
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run([str(launcher), "--help"], cwd=directory, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("usage: reel-context", result.stdout)
        self.assertIn("transcribe", result.stdout)
        self.assertIn("inspect", result.stdout)
