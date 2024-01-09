#!/usr/bin/python3
class MyList(list):
  def print_sorted(self):
    """
    print the list in ascending order.

    Return:
    none
    """
    sorted_list = sorted(self)
    print(sorted_list)
