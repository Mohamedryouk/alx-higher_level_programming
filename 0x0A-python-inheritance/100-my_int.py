#!/usr/bin/python3
"""
contains the class myint
"""


class MyInt(int):
    """rebel version of an int"""
    def __new__(cls, *args, **kwargs):
        """create instance of class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        return int(self) == other
