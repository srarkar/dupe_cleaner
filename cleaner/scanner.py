# recursively scan provided directory for dupes
# use current directory (pwd) if not provided
# take metadata from files and use it for quick comparisons 
# e.g. files of different sizes cannot be dupes

import os
from cleaner import metadata
from pathlib import Path

def scan_directory(path: Path, recursive=True):
    file_lst = []
    if (recursive):
        iterator = path.rglob("*")
    else:
         iterator = path.iterdir()

    # TODO: add flag for looking for hidden files or not ("-h")
    for file_path in iterator:
        if file_path.is_file() and not metadata.is_effectively_hidden(file_path):
                file_lst.append(metadata.get_file_metadata(file_path))
    return file_lst
