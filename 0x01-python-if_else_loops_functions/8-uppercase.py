#!/usr/bin/python3
def uppercase(_str):
    result = ""
    low = range(97, 123)
    for char in _str:
        if ord(char) in low:
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{:s}".format(result))
