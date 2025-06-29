import unittest
import tempfile
import subprocess
from pathlib import Path
import os

# run with python3 -m unittest discover tests
class TestDuplicateCleaner(unittest.TestCase):
    def test_multiple_duplicate_groups(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            tmpdir = Path(tmpdirname)

            # Define test file groups
            file_groups = {
                "group1": [("apple.txt", "fruit"), ("banana.txt", "fruit")],
                "group2": [("dog.txt", "animal"), ("cat.txt", "animal"), ("mouse.txt", "animal")],
                "unique": [("space.txt", "galaxy")]
            }

            # Create the files
            for group in file_groups.values():
                for filename, content in group:
                    (tmpdir / filename).write_text(content)

            # Run the duplicate cleaner
            subprocess.run(["python3", "main.py", str(tmpdir)], check=True)

            # Group1: Only one real file should remain
            self._check_duplicate_group(tmpdir, ["apple.txt", "banana.txt"])

            # Group2: Only one real file should remain
            self._check_duplicate_group(tmpdir, ["dog.txt", "cat.txt", "mouse.txt"])

            # Unique file: Should remain untouched
            space = tmpdir / "space.txt"
            self.assertTrue(space.exists())
            self.assertFalse(space.is_symlink())

    def _check_duplicate_group(self, base_path: Path, filenames: list[str]):
        real_files = []
        symlinks = []

        for fname in filenames:
            fpath = base_path / fname
            self.assertTrue(fpath.exists(), f"{fpath} should exist")
            if fpath.is_symlink():
                symlinks.append(fpath)
            else:
                real_files.append(fpath)

        # Only one real file, rest are symlinks
        self.assertEqual(len(real_files), 1, f"Expected 1 real file, found {len(real_files)}")
        self.assertGreaterEqual(len(symlinks), 1, f"Expected symlinks in group {filenames}")

        # All symlinks should point to the real file
        for link in symlinks:
            target = os.readlink(link)
            self.assertEqual(Path(target).resolve(), real_files[0].resolve(),
                f"{link} should point to {real_files[0]}")

