# this will handle displaying the summary of changes from running the cli tool

def print_report(storage: int, files: list):
    # maybe files can be a dictionary, where it is mapped to the storage?
    # print files that were deleted
    print("Deleted files:")
    for file in files:
        print(" " + file)
    print("Disk space cleared:")
    print(" " + str(storage) + " bytes")