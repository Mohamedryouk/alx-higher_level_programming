#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    total = sum(map(int, arguments))
    print(f"{total}")
