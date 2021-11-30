import pack
import unpack

def main():
    cmd = input("box > ")
    if cmd == "pack":
        pack.this("test.txt")
    elif cmd == "unpack":
        unpack.this("test.txt.box")



# Main Loop
if __name__ == "__main__":
    main()