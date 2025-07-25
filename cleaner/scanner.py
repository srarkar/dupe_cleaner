# recursively scan provided directory for dupes
# use current directory (pwd) if not provided
# take metadata from files and use it for quick comparisons 
# e.g. files of different sizes cannot be dupes

from cleaner import metadata
from pathlib import Path

def scan_directory(path: Path, recursive=True, hidden=False):
    file_lst = []
    if (recursive):
        iterator = path.rglob("*")
    else:
         iterator = path.iterdir()

    for file_path in iterator:
        if file_path.is_file():
            if hidden or not metadata.is_hidden(file_path):
                file_lst.append(metadata.get_file_metadata(file_path))
    return file_lst
