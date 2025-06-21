# simply computes hashes of files (NOT compare them)
# consider various hashing protocols (MD5, SHA256 -- slower but very secure? even SHA348 or 512)
# security is not really a concern --  focus on a protocol that works for large files
import hashlib

# returns hash of file located at provided path
def compute_hash(path_to_file):
    hash_obj = hashlib.sha256()
    input_data = "This is the data to be hashed."
    hash_obj.update(input_data.encode('utf-8'))
    hash_obj = hash_obj.hexdigest()
    return hash_obj