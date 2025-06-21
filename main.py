# initial commit
# this is the main file -- reads the user input (directory to scan)
#  - calls on files in cleaner/ for specific actions (recursive directory scan)
#  - uses hash values and comparisons (hasher.py + detector.py) to determine if a file is a dupe
#  - calls on actions.py to delete or archive if dupe is found
#  - call on reporter.py when everything is done; display the storage that was cleared or archived, and possibly list file names