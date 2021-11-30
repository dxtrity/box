import os

def just_the_file(file):
        with open(file, "r") as f:
            filename = str(os.path.basename(f.name))
            return filename

def get_filetype(file):
    with open(file, "r") as f:
        filename = os.path.basename(f.name).split(".")
        filetype = str(filename[1])
        return filetype

def get_dirname(file):
    with open(file, "r") as f:
        filename = os.path.basename(f.name).split(".")
        dirname = str(filename[0])
        return dirname

file = just_the_file("test.txt")
filename = get_dirname("test.txt")
filetype = get_filetype("test.txt")

def make_box_file():
    global filename
    global filetype

    with open(f"{filename}.box", "w") as f:
        f.write(f"box$")
        f.write(f"{filename}$")
        f.write(f".{filetype}")

def this(file):
    make_box_file()