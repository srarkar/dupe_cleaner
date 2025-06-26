# handle what we actually do to the files -- delete, archive
from sys import os

# given two files, one of which is the original and the other a clone, delete the clone and add a softlink to the original
# note that the parameters are FileMetadata objects
def delete_file(original_file, duplicate_file):
    try:
        os.remove(duplicate_file.path)
        os.symlink(src=original_file.path, dst=duplicate_file.path)
    except Exception as e:
        print(f"Failed to create symlink from {duplicate_file.path} to {original_file.path}: {e}")


# given a list of FileMetadata Objects, all of which are duplicates of each other, find the one with the most recent timestamp/mtime
# delete the rest, and return a list containing the deleted files for records.py
def delete_dupes(file_lst):

    # Find the file with the most recent modification time
    most_recent_file = max(file_lst, key=lambda f: f.timestamp)
    ## now, most_recent_file is the file that was modified most recently. delete everything else
    # pop it, and delete everything else
    file_lst.remove(most_recent_file)
    for file in file_lst:
        delete_file(most_recent_file, file)
    return file_lst # return all the files that have been deleted, for bookeeping
