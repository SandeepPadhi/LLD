"""
Python File Handling Reference
==============================
A comprehensive reference for file operations in Python
"""

# ----- Basic File Operations -----

# Opening a file
file = open("filename.txt", "r")  # Opens file for reading (default mode)
file.close()  # Always close files when done

# Using 'with' statement (recommended - automatically handles closing)
with open("filename.txt", "r") as file:
    data = file.read()  # Whole file as a string

# ----- File Open Modes -----

# "r"  - Read (default)
# "w"  - Write (creates new file or truncates existing file)
# "a"  - Append (creates new file or appends to existing file)
# "x"  - Exclusive creation (fails if file already exists)
# "b"  - Binary mode
# "t"  - Text mode (default)
# "+"  - Read and write

# Examples:
with open("file.txt", "r") as f:  # Read text
    pass

with open("file.bin", "rb") as f:  # Read binary
    pass

with open("file.txt", "w") as f:  # Write text (create/overwrite)
    pass

with open("file.bin", "wb") as f:  # Write binary (create/overwrite)
    pass

with open("file.txt", "a") as f:  # Append text
    pass

with open("file.txt", "r+") as f:  # Read and write
    pass

with open("file.txt", "w+") as f:  # Read and write (truncate first)
    pass

# ----- Reading From Files -----

with open("file.txt", "r") as file:
    # Read the entire file
    content = file.read()
    
    # Read fixed number of characters
    file.seek(0)  # Go to the beginning of the file
    chunk = file.read(5)  # Read 5 characters
    
    # Read line by line
    file.seek(0)
    first_line = file.readline()  # Read single line
    
    # Read all lines into a list
    file.seek(0)
    lines = file.readlines()  # Returns list of lines with \n at the end
    
    # Iterate through lines (memory efficient)
    file.seek(0)
    for line in file:
        print(line.strip())  # strip() removes the newline character

# ----- Writing To Files -----

with open("file.txt", "w") as file:
    # Write a string
    file.write("Hello, World!\n")
    
    # Write multiple lines
    file.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])

# ----- File Pointer Positioning -----

with open("file.txt", "r+") as file:
    # Get current position
    position = file.tell()
    
    # Change position (seek from beginning)
    file.seek(10)  # Move to 10th byte
    
    # Seek from current position
    file.seek(5, 1)  # Move 5 bytes forward from current position
    
    # Seek from end
    file.seek(-5, 2)  # Move 5 bytes before the end

# ----- File Properties and Methods -----

with open("file.txt", "r") as file:
    # Check if file is closed
    is_closed = file.closed  # False inside the with block, True outside
    
    # Get file name
    name = file.name
    
    # Get file mode
    mode = file.mode
    
    # Check if file is readable/writable
    can_read = file.readable()
    can_write = file.writable()
    
    # Flush the write buffer
    file.flush()
    
    # Truncate file to specified size
    file.truncate(100)  # Truncate to 100 bytes

# ----- Working with Binary Files -----

import struct

with open("binary.dat", "wb") as file:
    # Write binary data
    file.write(b"Binary data")  # b prefix for bytes
    
    # Pack binary data
    packed = struct.pack('i', 42)  # 'i' for integer
    file.write(packed)

with open("binary.dat", "rb") as file:
    # Read binary data
    binary_data = file.read(10)
    
    # Unpack binary data
    int_data = struct.unpack('i', file.read(4))[0]

# ----- OS Module File Operations -----

import os

# Check if file exists
exists = os.path.exists("file.txt")

# Get file size
size = os.path.getsize("file.txt")

# Get absolute path
abs_path = os.path.abspath("file.txt")
