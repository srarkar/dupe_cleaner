# groups file by hash values (by calling on hasher.py) to determine which files need to be deleted. 

# use a dictionary, where the key is the hash, and the value is a list of FileMetadata objects
from cleaner import metadata, hasher


# returns a dictionary
# keys: hash (sha256)
# values: a list of FileMetadata objects containing all the files whose hash values are the respective key
# automatically removes keys that only have one value for a specific hash, meaning no duplicate exists for it
def group_by_hash(file_lst):
    hash_to_file = {}
    for file in file_lst:
        hash = hasher.compute_hash(file.path)
        if hash in hash_to_file:
            hash_to_file[hash].append(file)
        else:
            hash_to_file[hash] = [file]
    
    for hash in list(hash_to_file):
        if len(hash_to_file[hash]) <= 1:
            hash_to_file.pop(hash)
    return hash_to_file


# returns a dictionary
# keys: file size in bytes
# values: a list of FileMetadata objects containing all the files that share a specific size
# automatically removes keys that only have one value for a specific size, meaning no duplicate exists for it
# TODO: try to use in conjunction with group_by_hash to only check files that have the same size for being duplicates
def group_by_size(file_lst):
    size_to_file = {}
    for file in file_lst:
        size = file.size
        if size in size_to_file:
            size_to_file[size].append(file)
        else:
            size_to_file[size] = [file]
    for hash in list(hash_to_file):
        if len(hash_to_file[hash]) <= 1:
            hash_to_file.pop(hash)
    return hash_to_file
    
