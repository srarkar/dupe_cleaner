# this will handle displaying the summary of changes from running the cli tool

def print_report(files: list):
    # given a list of files, call on calculate report to get total storage deleted
    # things to consider printing:
    # total storage cleared
    # number of duplicate groups found -- this is the number of keys in files_by_hash!
    # number of files deleted
    # number of symlinks made
    pass
    

def calculate_report(files: lst):
    # returns a dictionary with keys being fields like storage_saved, num_files_deleted, etc. called on by print_report
    pass