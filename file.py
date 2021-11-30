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