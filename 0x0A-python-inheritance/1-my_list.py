#!/usr/bin/python3
class MyList(list):
  def print_sorted(self):
    """
    print the list in ascending order.

    Return:
    none
    """
    print(sorted(self.copy()))
