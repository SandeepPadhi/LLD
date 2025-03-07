


with open("log_file.txt",'+w') as f:
    f.write("Hello sandeep\n")
    f.write("what'sapp")
    f.seek(0)
    f.append("appending yar")
