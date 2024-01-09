#!/usr/bin/python3
"""
This module check if its instance of inherited class or specified class
"""
def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class) or type(obj) is is_kind_of_class
