# creating directories

import os

# Directory
directory = "test_dir"

# Parent directory (folder before the one your making)
parent_directory = "C:/Users/Julie/Documents"

# Path
path = os.path.join(parent_directory, directory)

# Create Dir
os.mkdir(path)

# Create a message so you know it works

print(f" directory {directory} created in {parent_directory}")

