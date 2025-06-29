# this will handle displaying the summary of changes from running the cli tool

def print_report(deleted_files, files_by_hash, failed_links):
    # given a list of files, call on calculate report to get total storage deleted
    # things to consider printing:
    # total storage cleared
    # number of duplicate groups found -- this is the number of keys in files_by_hash!
    # number of files deleted
    # number of symlinks made
    pass
    

def calculate_report(deleted_files, files_by_hash, failed_links):
    deleted_files_info = {}
    storage_saved = 0

    dupe_groups = len(files_by_hash.keys())
    num_files_deleted = len(deleted_files)
    for file in deleted_files:
        storage_saved += file.size
    
    deleted_files_info["storage"] = storage_saved
    deleted_files_info["num_deleted"] = num_files_deleted
    deleted_files_info["num_duplicate_groups"] = dupe_groups
    deleted_files["failed_symlinks"] = failed_links
    return deleted_files