# recursively scan provided directory for dupes
# use current directory (pwd) if not provided
# take metadata from files and use it for quick comparisons 
# e.g. files of different sizes cannot be dupes

import os

def scan_directory(path):
    file_lst = []
    
