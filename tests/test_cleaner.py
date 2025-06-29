import unittest
import tempfile
import subprocess
from pathlib import Path
import os
from cleaner import metadata
import shutil

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

    def test_is_hidden_on_files_and_dirs(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            tmpdir = Path(tmpdirname)

            # Create visible file and hidden file
            visible_file = tmpdir / "visible.txt"
            hidden_file = tmpdir / ".hidden.txt"
            visible_file.write_text("visible")
            hidden_file.write_text("hidden")

            # Create visible directory and hidden directory
            visible_dir = tmpdir / "visible_dir"
            hidden_dir = tmpdir / ".hidden_dir"
            visible_dir.mkdir()
            hidden_dir.mkdir()

            # Create files inside dirs
            (visible_dir / "file.txt").write_text("inside visible dir")
            (hidden_dir / "file.txt").write_text("inside hidden dir")

            # Test files
            self.assertFalse(metadata.is_hidden(visible_file))
            self.assertTrue(metadata.is_hidden(hidden_file))

            # Test directories themselves
            self.assertFalse(metadata.is_hidden(visible_dir))
            self.assertTrue(metadata.is_hidden(hidden_dir))

            # Test files inside directories with is_effectively_hidden()
            self.assertFalse(metadata.hidden_parent(visible_dir / "file.txt"))
            self.assertTrue(metadata.hidden_parent(hidden_dir / "file.txt"))
    def test_recursive_vs_local_scan(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            tmpdir = Path(tmpdirname)

            # Create files in root and in subdirectory
            (tmpdir / "rootfile.txt").write_text("root")
            subdir = tmpdir / "subdir"
            subdir.mkdir()
            (subdir / "subfile.txt").write_text("subdir")

            # Run main.py with recursive scan (default)
            subprocess.run(["python3", "main.py", str(tmpdir)], check=True)

            # Both files should exist (one real, one symlink if duplicates)
            self.assertTrue((tmpdir / "rootfile.txt").exists())
            self.assertTrue((subdir / "subfile.txt").exists())

            # Now run with local scan -l flag (no recursion)
            # First, restore original files by deleting and recreating them
            shutil.rmtree(tmpdir)
            tmpdir.mkdir()
            (tmpdir / "rootfile.txt").write_text("root")
            subdir.mkdir()
            (subdir / "subfile.txt").write_text("subdir")

            subprocess.run(["python3", "main.py", str(tmpdir), "-l"], check=True)

            # rootfile.txt should exist, subfile.txt should exist but not scanned or symlinked
            self.assertTrue((tmpdir / "rootfile.txt").exists())
            self.assertTrue((subdir / "subfile.txt").exists())

            # Since local scan ignores subdir, subfile.txt should remain untouched (not replaced by symlink)
            # Check that subfile.txt is NOT a symlink
            self.assertFalse((subdir / "subfile.txt").is_symlink())

    def test_dry_run_no_deletion(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            tmpdir = Path(tmpdirname)

            # Create duplicate files
            (tmpdir / "file1.txt").write_text("duplicate content")
            (tmpdir / "file2.txt").write_text("duplicate content")

            # Run main.py with --dry-run flag
            subprocess.run(["python3", "main.py", str(tmpdir), "--dry-run"], check=True)

            # Both files should still exist and be regular files (no deletion, no symlinks)
            f1 = tmpdir / "file1.txt"
            f2 = tmpdir / "file2.txt"
            self.assertTrue(f1.exists())
            self.assertTrue(f2.exists())
            self.assertFalse(f1.is_symlink())
            self.assertFalse(f2.is_symlink())
