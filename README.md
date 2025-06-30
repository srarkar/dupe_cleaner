# dupe_cleaner

## Overview
CLI Tool that finds and removes duplicate files

in-progress

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
After cloing 
