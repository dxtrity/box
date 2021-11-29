import os
import shutil

def get_data(a):
    with open(a,"r") as r:
        content = r.read()
        return content

def pack(a):
    content = get_data(a)

    with open(a, "w") as f:

        filename = os.path.basename(f.name).split(".")
        dirname = str(filename[0])
        filetype = str(filename[1])
        
        packed_file = str(f"{dirname}.box")
        
        f.write(f"$.{filetype}")
        f.write(f"${content}")

        shutil.copy(a,packed_file)