# compute hashes of files, and compare them
import hashlib


# returns hash of file located at provided path
# hash protocol is SHA256 for security
def compute_hash(path_to_file):
    # arbitrary buffer size
    BUF_SIZE = 65536  # 64 kb chunks

    hash_obj = hashlib.sha256()
    
    with open(path_to_file, 'rb') as file:
        while True:
            data = file.read(BUF_SIZE)
            if not data:
                break
            hash_obj.update(data)
    return hash_obj.hexdigest()

def compare_hashes(file1, file2):
    file1_hash = compute_hash(file1)
    file2_hash = compute_hash(file2)
    return file1_hash == file2_hash