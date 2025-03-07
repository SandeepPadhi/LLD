# File Modes in Python - Explanation and Examples

# Read Modes

# 'r': Read (default)
# Opens a file for reading only.
# Will raise FileNotFoundError if the file does not exist.
# Example:
try:
    with open("read_example.txt", "r") as f:
        content = f.read()  # Reads the entire file content
        print("Read mode ('r'):", content)
except FileNotFoundError:
    print("File 'read_example.txt' not found.")

# 'rt': Read text (default)
# Opens a file for reading in text mode.
# Will raise FileNotFoundError if the file does not exist.
# Example: (Same as 'r' for text files)
try:
    with open("read_example.txt", "rt") as f:
        content = f.read()  # Reads the entire file content
        print("Read text mode ('rt'):", content)
except FileNotFoundError:
    print("File 'read_example.txt' not found.")

# 'rb': Read binary
# Opens a file for reading in binary mode.
# Will raise FileNotFoundError if the file does not exist.
# Example (reading a binary file, e.g., an image):
# (Requires a binary file to exist)
# try:
#     with open("image.jpg", "rb") as f:
#         binary_data = f.read()
#         print("Read binary mode ('rb'):", type(binary_data)) # Will print <class 'bytes'>
# except FileNotFoundError:
#     print("Binary file 'image.jpg' not found.")

# Write Modes

# 'w': Write
# Opens a file for writing only. Creates a new file or truncates an existing file.
# TRUNCATES existing file.
# Example:
with open("write_example.txt", "w") as f:
    f.write("This is written in 'w' mode.")

# 'wt': Write text
# Opens a file for writing in text mode.
# TRUNCATES existing file.
# Example: (Same as 'w' for text files)
with open("write_example.txt", "wt") as f:
    f.write("This is written in 'wt' mode.")

# 'wb': Write binary
# Opens a file for writing in binary mode.
# TRUNCATES existing file.
# Example: (writing binary data)
# with open("binary_example.bin", "wb") as f:
#     f.write(b"\x00\x01\x02") #writing byte objects.

# Append Modes

# 'a': Append
# Opens a file for appending. Creates a new file if it doesn't exist.
# Does NOT truncate.
# Example:
with open("append_example.txt", "a") as f:
    f.write("\nThis line is appended in 'a' mode.")

# 'at': Append text
# Opens a file for appending in text mode.
# Does NOT truncate.
# Example: (Same as 'a' for text files)
with open("append_example.txt", "at") as f:
    f.write("\nThis line is appended in 'at' mode.")

# 'ab': Append binary
# Opens a file for appending in binary mode.
# Does NOT truncate.
# Example: (appending binary data)
# with open("binary_example.bin", "ab") as f:
#     f.write(b"\x03\x04\x05")

# Read/Write Modes (Update Modes)

# 'r+': Read and write
# Opens a file for both reading and writing. The file pointer is placed at the beginning.
# Does NOT truncate.
# Will raise FileNotFoundError if the file does not exist.
# Example:
try:
    with open("read_write_example.txt", "r+") as f:
        f.write("Updated at start.")
        f.seek(0)
        print("Read/write mode ('r+'):", f.read())
except FileNotFoundError:
    print("File read_write_example.txt not found")

# 'w+': Write and read
# Opens a file for both writing and reading. Creates a new file or truncates an existing file.
# TRUNCATES existing file.
# Will create the file if it does not exist.
# Example:
with open("write_read_example.txt", "w+") as f:
    f.write("Written and then read.")
    f.seek(0)
    print("Write/read mode ('w+'):", f.read())

# 'a+': Append and read
# Opens a file for both appending and reading. The file pointer is placed at the end.
# Does NOT truncate.
# Will create the file if it does not exist.
# Example:
with open("append_read_example.txt", "a+") as f:
    f.write("Appended and then read.")
    f.seek(0)
    print("Append/read mode ('a+'):", f.read())

# Exclusive Creation Mode

# 'x': Exclusive creation
# Opens a file for exclusive creation. If the file already exists, the operation fails.
# Does NOT truncate (but will fail if the file exists).
# Example:
try:
    with open("exclusive_example.txt", "x") as f:
        f.write("Created exclusively.")
    print("File created exclusively.")
except FileExistsError:
    print("File 'exclusive_example.txt' already exists.")

# 'xt', 'xb' same as 'x' but specifying text or binary.

# Working with Large Files
def read_large_file(file_path):
    try:
        with open(file_path, 'r') as f:
            for line in f: #Reads file line by line.
                #Process the line here
                print(line.strip()) #Example processing, prints each line.
    except FileNotFoundError:
        print(f"File {file_path} not found.")

# Example usage for large files:
# read_large_file("large_file.txt")

# Regex Analysis Example
import re
def analyze_log_file(log_file_path):
    error_count = 0
    warning_count = 0
    try:
        with open(log_file_path, 'r') as f:
            for line in f:
                if re.search(r'ERROR', line):
                    error_count += 1
                elif re.search(r'WARNING', line):
                    warning_count += 1
    except FileNotFoundError:
        print(f"Log file {log_file_path} not found.")
        return

    print(f"Error count: {error_count}")
    print(f"Warning count: {warning_count}")

# Example log file creation for regex testing.
with open("logfile.txt", "w") as f:
    f.write("2023-11-20 10:00:00 - INFO - System started\n")
    f.write("2023-11-20 10:01:00 - ERROR - Database connection failed\n")
    f.write("2023-11-20 10:02:00 - WARNING - Low disk space\n")
    f.write("2023-11-20 10:03:00 - ERROR - Invalid user input\n")

analyze_log_file("logfile.txt")
