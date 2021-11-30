import os

def this(file):
    with open(file, "r") as f:
        pragma = os.path.basename(f.name).split(".")

        filename = pragma[0]
        filetype = pragma[1]
        size = os.path.getsize(file)
        file_check = os.path.isfile(file)

        print(f"File Name: {filename}")
        print(f"File Type: {filetype}")
        print(f"File Size: {size}")
        print(f"File: {file_check}")
