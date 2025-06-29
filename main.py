# this is the main file -- reads the user input (directory to scan)
#  - calls on files in cleaner/ for specific actions (recursive directory scan)
#  - uses hash values and comparisons (hasher.py + detector.py) to determine if a file is a dupe
#  - calls on actions.py to delete if dupe is found
#  - call on reporter.py when everything is done; display the storage that was cleared or archived, and possibly list file names
import sys
import os
from pathlib import Path
from cleaner import scanner, reporter, detector, metadata, actions


def parse_args(argv):
    args_lst = []
    argc = 0
    for arg in argv:
        if (arg != "main.py"):
            args_lst.append(arg)
            argc += 1
    return args_lst, argc

def flag_handling(args_lst):
    flag_dictionary = {}
    if "-l" in args_lst:
        flag_dictionary["recursive"] = False
        args_lst.remove("-l")
    else:
        flag_dictionary["recursive"] = True
    
    if "--dry-run" in args_lst:
        flag_dictionary["dry_run"] = True
        args_lst.remove("--dry-run")
    else:
        flag_dictionary["dry_run"] = False
    
    if "-f" in args_lst:
        flag_dictionary["file_names"] = True
        args_lst.remove("-f")
    else:
        flag_dictionary["file_names"] = False

    if args_lst != []:
        print(f"Invalid argument(s): {args_lst}")
        print("Continuing operations...")
    return flag_dictionary
    
    

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
    print(f"Path: {path}")

    ### use scanner to get a list of all files in provided path, using recursive descent
    ## TODO: abstract flag handling into helper
    flags = flag_handling(args_lst)

    file_lst = scanner.scan_directory(path, flags["recursive"])

    files_by_size = (detector.group_by_size(file_lst))


    # the size step is optional but should reduce computation
    files_by_hash = {}
    for size_group in files_by_size.values():
        group = detector.group_by_hash(size_group)
        files_by_hash.update(group)
    # files_by_hash has keys that are hash values, with values being a list a FileMetadata objects sharing the hash
    ### then, call actions to delete or archive files that are duplicates.
    deleted_files = []
    failed_links = 0
    for hash in files_by_hash.keys():
        group_deleted, flinks = actions.delete_dupes(files_by_hash[hash], flags["dry_run"])
        deleted_files += group_deleted
        failed_links += flinks

    reporter.print_report(deleted_files, files_by_hash, failed_links, flags)


        



