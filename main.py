import bpm

def main():
    cmd = input("box > ")
    if cmd == "pack":
        bpm.pack("test.txt")
    elif cmd == "unpack":
        bpm.unpack("test.txt.box")



# Main Loop
if __name__ == "__main__":
    main()