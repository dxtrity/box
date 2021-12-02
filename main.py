import pack
import query
import ship
import install

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
    elif cmd == "ship":
        ship.this("Dev Defined Argument","Dev Defined Argument")
        print("")
        main()
    elif cmd == "install":
        install.this("Dev Defined Argument")
        print("")
        main()
    else:
        print("That is now a valid command. Run 'box help' for help.")
        main()




# Main Loop
if __name__ == "__main__":
    main()