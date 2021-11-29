import shutil
import os

# Pack files
def pack(a):
    b = f"{a}.box"
    shutil.copy(a,b)

# Unpack files
def unpack(a):
    with open(a) as f:
        filename = os.path.basename(f.name).split(".")

        dirname = str(filename[0])
        filetype = str(filename[1])

        unpacked_file = str(f"{dirname}.{filetype}")

        shutil.copy(a,unpacked_file)

# Ship files
def ship(a,b):
    print("This is not yet implemented.")
    print("")
    print(a)
    print(b)

# Install files
def install(a):
    print("This is not yet implemented.")
    print("")
    print(a)

# USED FOR DEBUGGING
if __name__ == "__main__":
    #install("this is cool")
    print("Debugger is not setup. Head to bottom of script and extend it.")