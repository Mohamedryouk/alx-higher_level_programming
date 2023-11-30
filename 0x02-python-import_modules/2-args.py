#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sys.argv.pop(0)
    numberOfargs = len(sys.argv)
    if numberOfargs == 0:
        print("0 arguments.")
    elif numberOfargs == 1:
        print("1 argument:")
        print("{:d}: {}".format(len(sys.argv), sys.argv[0]))
    else:
        print("{:d} arguments:".format(numberOfargs))
        index = 1
        for arguments in sys.argv:
            print("{:d}: {}".format(index, arguments))
            index += 1
