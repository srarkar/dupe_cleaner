# initial commit
# this is the main file -- reads the user input (directory to scan)
#  - calls on files in cleaner/ for specific actions (recursive directory scan)
#  - uses hash values and comparisons (hasher.py + detector.py) to determine if a file is a dupe
#  - calls on actions.py to delete or archive if dupe is found
#  - call on reporter.py when everything is done; display the storage that was cleared or archived, and possibly list file names

import sys
import os
from pathlib import Path
from cleaner import scanner, hasher, reporter, detector, metadata

### sys testing
def parse_args(argv):
    args_lst = []
    argc = 0
    for arg in argv:
        if (arg != "main.py"):
            args_lst.append(arg)
            argc += 1
    return args_lst, argc

if __name__ == "__main__":
    args_lst, argc = parse_args(sys.argv)

    # use current directory if not provided
    if args_lst == []:
        print("Path to directory not provided. Using current directory...")
        path = os.getcwd()
    else:
        path = args_lst[0]
        if  not os.path.isdir(path):
            print(f"{path} is not a directory.")
            query = input("Use current director instead? y/n\n")
            if query == "y" or query == "ye" or query == "yes" or query == "yurr":
                path = os.getcwd()
            else:
                sys.exit(1)
    path = Path(path)
    print(path)

    ### use scanner to get a list of all files in provided path, using recursive descent
    ## TODO: check for if the user adds a flag for recursive or not (such as -l for "local"?)
    if "-l" in args_lst:
        recursive = False
        args_lst.pop(args_lst.index("-l"))
    else:
        recursive = True
    file_lst = scanner.scan_directory(path, recursive)
    for file in file_lst:
        pass
        #print(file.name)


    files_by_size = (detector.group_by_size(file_lst))
    # the size step is optional but should reduce computation
    files_by_hash = {}
    for size_group in files_by_size.values():
        group = detector.group_by_hash(size_group)
        files_by_hash.update(group)
    print(files_by_hash)

    ### then, call actions to delete or archive files that are duplicates.
    # When choosing which one to delete, delete the older one based on timestamp field



