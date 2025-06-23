# used to acccess file metadata such as path, file size, what time it was accessed or moved, hidden, etc
from dataclasses import dataclass
from pathlib import Path
import os

@dataclass
class FileMetadata:
    path: Path
    size: int
    timestamp: float

# used as a constructor to return a FileMetadata object
def get_file_metadata(path: Path):
    stats = path.stat()
    return FileMetadata(
        path=path,
        size = stats.st_size,
        mtime = stats.st_mtime
    )

def is_hidden(path: Path):
    if os.name == "posix": # macOS/Linux
        return path.name.startswith(".")
    elif os.name == "nt":  # Windows
        ## NOT IMPLEMENTED YET 
        ## Use ctypes.windll.kernel32.GetFileAttributesW(path) to get attributes
        # Check if the 0x2 (hidden) bit is set
        return False


    

path = Path("/Users/ricksarkar/Sum25/Projects/dupe_cleaner/tests/.main.py")
print(is_hidden(path))