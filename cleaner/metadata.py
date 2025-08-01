# used to acccess file metadata such as path, file size, what time it was accessed or moved, hidden, etc
from dataclasses import dataclass
from pathlib import Path
import os

@dataclass
class FileMetadata:
    path: Path
    size: int
    timestamp: float

    @property
    def name(self):
        return self.path.name

# used as a constructor to return a FileMetadata object
def get_file_metadata(path: Path):
    stats = path.stat()
    return FileMetadata(
        path=path,
        size = stats.st_size,
        timestamp = stats.st_mtime
    )

def is_hidden(path: Path):
    if os.path.isdir(path):
        return any(part.startswith(".") for part in path.parts)  # important for not recursing into subdirs like .git
    if os.name == "posix": # macOS/Linux
        return path.name.startswith(".")
    elif os.name == "nt":  # Windows
        ### this is completely untested -- use at your own peril !!
        FILE_ATTRIBUTE_HIDDEN = 0x2
        GetFileAttributesW = ctypes.windll.kernel32.GetFileAttributesW
        GetFileAttributesW.argtypes = [ctypes.c_wchar_p]
        GetFileAttributesW.restype = ctypes.c_uint32

        attrs = GetFileAttributesW(str(path))
        if attrs == 0xFFFFFFFF:
            raise ctypes.WinError()
        return bool(attrs & FILE_ATTRIBUTE_HIDDEN)
    