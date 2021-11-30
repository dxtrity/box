import pack
import query

def main():
    _cmd = input("box > ").split()
    cmd = _cmd[0]
    op = _cmd[1]
    if cmd == "pack":
        print("Finishing your package up...")
        pack.this(f"{op}")
        print(f"Created box file for {op}!")
        print("")
        main()
    elif cmd == "query":
        query.this(f"{op}")
        print("")
        main()



# Main Loop
if __name__ == "__main__":
    main()