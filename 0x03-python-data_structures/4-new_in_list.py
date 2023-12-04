#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newlist = list.copy(my_list)
    if idx >= 0:
        newlist[idx] = element
    elif idx < len(my_list):
        newlist[idx] = element
    return newlist
