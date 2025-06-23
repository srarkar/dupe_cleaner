
file_path = "new_file.txt"
try:
    with open(file_path, 'x') as file:
        file.write("Testing out hashing")
    print(f"File '{file_path}' created successfully.")
except FileExistsError:
    print(f"File '{file_path}' already exists.")
