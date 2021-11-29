import pack
import unpack

def main():
    cmd = input("box > ")
    if cmd == "pack":
        pack.pack("test.txt")
    elif cmd == "unpack":
        unpack.unpack("test.txt.box")



# Main Loop
if __name__ == "__main__":
    main()