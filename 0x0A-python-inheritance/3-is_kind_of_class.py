#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class) or type(obj) is is_kind_of_class  