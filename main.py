import pack
import query

def main():
    _cmd = input("box > ").split()
    cmd = _cmd[0]
    op = _cmd[1]
    if cmd == "pack":
        print("Finishing your package up...")
        pack.this(f"{op}")
        print("All set and all ready to go!")
        print("")
        main()
    elif op == "query":
        query.this(f"{op}")
        print("")
        main()



# Main Loop
if __name__ == "__main__":
    main()