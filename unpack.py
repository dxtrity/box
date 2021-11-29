import os
import shutil

def unpack(a):
    with open(a, "r") as f:
        filename = os.path.basename(f.name).split(".")

        dirname = str(filename[0])
        filetype = str(filename[1])

        unpacked_file = str(f"{dirname}.{filetype}")

        shutil.copy(a,unpacked_file)