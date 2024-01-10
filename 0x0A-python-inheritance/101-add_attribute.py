#!/usr/bin/python3
"""
Contains a function to add attribute
"""


def add_attribute(a_class, name, value):
    if hasattr(a_class, "__dic__"):
        setattr(a_class, name, value)
    else:
        raise TypeError("can't add new attribute")
