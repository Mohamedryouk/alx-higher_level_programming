#!/usr/bin/python3
def raise_exception():
    raise TypeError("This is a custom type exception.")
try:
    raise_exception()
except TypeError as e:
    print("Caught an exception:", e)
