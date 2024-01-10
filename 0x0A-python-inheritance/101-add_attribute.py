#!/usr/bin/python3
"""
Contains a function to add attribute
"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an obj if possible"""
    if not hasattr(obj, "__dic__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name ,value)
