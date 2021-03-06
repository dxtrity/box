import pack
import query
import ship
import install
import helpful

def main():
    _cmd = input("box > ").split()
    cmd = _cmd[0]
    op = _cmd[1]
    if cmd == "pack":
        print("Finishing your package up...")
        pack.this(op)
        print(f"Created box file for {op}!")
        print("")
        main()
    elif cmd == "query":
        query.this(op)
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
    elif cmd == "help" and op == "pack":
        helpful.help_pack()
        main()
    elif cmd == "help" and op == "me":
        helpful.help_cmd()
        main()
    elif cmd == "help" and op == "ship":
        helpful.help_ship()
        main()
    elif cmd == "help" and op == "install":
        helpful.help_install()
        main()
    elif cmd == "help" and op == "query":
        helpful.help_query()
        main()
    else:
        print("That is now a valid command. Run 'box help me' for help.")
        main()

# Main
if __name__ == "__main__":
    main()