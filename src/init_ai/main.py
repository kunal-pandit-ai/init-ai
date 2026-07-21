#----------------------
"""This is temp"""
#-----------------------
import sys
from .commands.hello import hello
from .commands.version import version
from .commands.who import who
from .commands.author import author

def main():
    if len(sys.argv) < 2:
        print("No command found!")
        return
    
    command = sys.argv[1]

    if command == "hello":
        hello()
    elif command == "version":
        version()
    elif command == "who":
        who()
    elif command == "author":
        author()
    elif command == "--help":
        print("""
Commands:-
        hello
        version
        who
        author
        --help
    """)
    else:
        print("Unknown command [use --help]")
        
if __name__ == "__main__":
    main()
