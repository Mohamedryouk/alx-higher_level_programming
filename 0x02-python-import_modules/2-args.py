#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    numberOfargs = len(arguments)

    if numberOfargs > 0:
        print(f"{numberOfargs} arguments :")
        for index, arg in enumerate(arguments, 1):
            print(f"{index}: {arg}")
    else:
        print(f"{numberOfargs} arguments .")
