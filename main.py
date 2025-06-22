# initial commit
# this is the main file -- reads the user input (directory to scan)
#  - calls on files in cleaner/ for specific actions (recursive directory scan)
#  - uses hash values and comparisons (hasher.py + detector.py) to determine if a file is a dupe
#  - calls on actions.py to delete or archive if dupe is found
#  - call on reporter.py when everything is done; display the storage that was cleared or archived, and possibly list file names

import sys
from cleaner import scanner, hasher, reporter

### sys testing
def parse_args(argv):
    args_lst = []
    arg_count = 0
    for arg in argv:
        if (arg != "main.py"):
            args_lst.append(arg)
            arg_count += 1
    print("\n")
    print(args_lst)
    print("num args: " + str(arg_count))
    print("\n")

if __name__ == "__main__":

  parse_args(sys.argv)

  # testing functions from cleaner/
  print("Report:")
  reporter.print_report(32, ["file1", "file2"])

  print("Hashing: ")
  print(hasher.compute_hash("/Users/ricksarkar/Sum25/Projects/dupe_cleaner/main.py"))