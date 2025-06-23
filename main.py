# initial commit
# this is the main file -- reads the user input (directory to scan)
#  - calls on files in cleaner/ for specific actions (recursive directory scan)
#  - uses hash values and comparisons (hasher.py + detector.py) to determine if a file is a dupe
#  - calls on actions.py to delete or archive if dupe is found
#  - call on reporter.py when everything is done; display the storage that was cleared or archived, and possibly list file names

import sys
import os
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
            if query == "y" or query == "yes":
                path = os.getcwd()
            else:
                sys.exit(1)
    print(path)

    ### use scanner to get a list of all files in provided path, using recursive descent
    # file_lst = scanner.scan_directory(path)

    ### call detector on this list which will hash all of them and group them by files with the same hash

    ### then, call actions to delete or archive files that are duplicates. When choosing which one to delete, delete the older one based on mtime



