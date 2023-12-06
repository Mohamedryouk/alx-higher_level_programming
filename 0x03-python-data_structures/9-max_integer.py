#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_vlaue = my_list[0]
    for i in my_list:
        if i > max_vlaue:
            max_vlaue = i
    return max_vlaue
