import file

def this(a):
    filename = file.get_dirname(a)
    filetype = file.get_filetype(a)

    with open(f"{filename}.box", "w") as f:
        f.write(f"box$")
        f.write(f"{filename}$")
        f.write(f".{filetype}")