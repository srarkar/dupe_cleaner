# handle what we actually do to the files -- delete, archive
import os
# given two files, one of which is the original and the other a clone, delete the clone and add a softlink to the original
# note that the parameters are FileMetadata objects
def delete_file(original_file, duplicate_file, dry_run):
    failed_links = 0
    try:
        if not dry_run:
            os.remove(duplicate_file.path)
            os.symlink(src=original_file.path, dst=duplicate_file.path)
            print(f"Deleting {duplicate_file.path} and linking to {original_file.path}")
        else:
            print(f"Would have deleted {duplicate_file.path} and linked to {original_file.path}")
    except Exception as e:
        print(f"Failed to create symlink from {duplicate_file.path} to {original_file.path}: {e}")
        failed_links += 1
    return failed_links


# given a list of FileMetadata Objects, all of which are duplicates of each other, find the one with the most recent timestamp/mtime
# delete the rest, and return a list containing the deleted files for records.py
def delete_dupes(file_lst, dry_run):
    failed_links = 0
    # Find the file with the most recent modification time
    most_recent_file = max(file_lst, key=lambda f: f.timestamp)
    ## now, most_recent_file is the file that was modified most recently. delete everything else
    # pop it, and delete everything else
    file_lst.remove(most_recent_file)
    for file in file_lst:
        failed_links += delete_file(most_recent_file, file, dry_run)
    return file_lst, failed_links # return all the files that have been deleted, for bookeeping
