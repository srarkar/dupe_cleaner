# compute hashes of files, and compare them
import hashlib


# returns hash of file located at provided path
# hash protocol is SHA256 for security
# returns None if hash fails to be computed -- mainly with opening the file
def compute_hash(path):
    if path is None:
        return 
    # arbitrary buffer size
    BUF_SIZE = 65536  # 64 kb chunks

    hash_obj = hashlib.sha256()
    try:
        with open(path, 'rb') as file:
            while True:
                data = file.read(BUF_SIZE)
                if not data:
                    break
                hash_obj.update(data)
        return hash_obj.hexdigest()
    except FileNotFoundError:
        print(f"Error -- File not found: {path}")
        return None
    except IsADirectoryError:
        print(f"Error -- Expected file, not directory: {path}")
        return None
    except PermissionError:
        print(f"Error -- You do not have permission to access this file: {path}")
        return None
    except Exception as e:
        print(f"Unknown error when accessing {path}: {e}")
        return None

# this can be used by actions.py or reporter.py to double check the hash after the file has been moved 
def validate_hash(path, expected_hash):
    if not path or not expected_hash:
        return False
    return compute_hash(path) == expected_hash

def compare_hashes(file1, file2):
    file1_hash = compute_hash(file1)
    file2_hash = compute_hash(file2)

    if not file1_hash or not file2_hash:
        return False
    
    return file1_hash == file2_hash