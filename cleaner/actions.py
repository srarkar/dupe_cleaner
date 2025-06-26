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
# delete the rest of them, calling on delete_file (above)
def delete_dupes(file_lst):
    pass
