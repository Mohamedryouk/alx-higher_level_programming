#!/usr/bin/python3
"""
This module contains function is_same_class
"""


def is_same_class(obj, a_class):
    """
    check for the obj if its exactly and instance of specified class.
    parameters:
    obj: The object to check.
    a_class: the class to compare.
    Returns:
    bool: True if it's instance of a_class, otherwise false
    """
    return type(obj) is a_class
