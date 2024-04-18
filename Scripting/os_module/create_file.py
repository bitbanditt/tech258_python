# creating files

import os

# Directory
directory = "test_dir"

# Parent directory (folder before the one your making)
parent_directory = "C:/Users/Julie/Documents"

# Path
path = os.path.join(parent_directory, directory)

# Filename

filename = "testfile.txt"

# Filepath

filepath = os.path.join(path, filename)

# Create the file (w for write)

with open(filepath, "w") as file1:
    toFile = "Contents of the file go here"
    file1.write(toFile)

# Check it works when run via terminal

print(f"File {filename} created in {directory} folder")