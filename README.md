# Duplicate File Cleaner

## Overview
`CLI` (Command-Line Interface) tool that finds and deletes duplicate files. Duplicates are found by hashing the contents of files following the `SHA256` protocol.
Files are first sorted by file size then by hash, since two files cannot be duplicates if their file sizes differ. 

When duplicate files are found, they are deleted based on which was modified the least recently. Thus, in a group of duplicate files, the one file survivor will be the one modified most recently. 

Note that when a file is deleted, a `symbolic link`, also known as a `softlink` or `symlink` is created between the deleted file and the survivor. 
If something referenced a file that was deleted by the tool, it will be redirected to the survivor automatically. 

## Flags:

These optional flags alter how the tool works, including the print outputs or what files it looks at when searching for duplicates.
  - `-l`: By default, the tool runs recursively, searching all non-hidden subdirectories found in the provided path. Adding `-l` (local) prevents the recursive descent, meaning that the tool will only delete duplicate files found in the provided directory and no subdirectories.
  - `-f`: After the tool finishes running, it outputs a report that includes information on the storage cleared, number of files removed, and more. To also display the exact file names that were deleted, include the `-f` flag
  - `-h`: By default, the tool ignores hidden files and directories. Including the `-h` flag will allow these files to be checked and deleted if duplicates are found.
  - `--dry-run`: A useful flag for finding duplicates but not deleting, or testing the command initially. This will _simulate_ a running of the tool, including the final report. However, no files will be moved or deleted. Pair with `-f` to display file names.

## Usage:
### Running from main.py:
Clone this repository by running ``git clone https://github.com/srarkar/dupe_cleaner.git``, followed by ``cd dupe_cleaner`` to enter the newly created directory.
Then, run ``python3 main.py [PATH] [FLAGS]`` to run the tool. 

### Use as CLI tool:
#### Requirements:
  - Python 3.6+ installed on your system
  - pip package manager installed
    
Clone this repository by running ``git clone https://github.com/srarkar/dupe_cleaner.git``, followed by ``cd dupe_cleaner`` to enter the newly created directory.
Then, run ``pip install .``
Now, you can run the ``dupecleaner [PATH] [FLAGS]`` CLI tool from anywhere within your terminal.

### Running test cases:
There are some tests in place that ascertain expected behavior of the duplicate file cleaner. After cloning the repository with ``git clone https://github.com/srarkar/dupe_cleaner.git``, run ``cd dupe_cleaner`` followed by ``cd tests`` to enter the `tests` subdirectory. From there, run ``python3 -m unittest discover -v tests`` to run the test cases. 
Feel free to add additional tests if you wish.

## Notes
  - Windows functionality regarding hidden file detection is currently untested. Core functionality should not be affected, but it is possible that hidden files that are not meant to be checked will be when the tool is ran on a Windows device.
  - Additionally, file metadata is not preseved upon deletion, even with the symlink creation. After the tool is run and symlinks are created, be careful with moving the remaining file (the survivor of the duplicates), as it may interfere with the symlinks that point to it. 
