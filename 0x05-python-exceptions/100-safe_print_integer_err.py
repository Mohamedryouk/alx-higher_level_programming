#!usr/bin/python3
import sys
"""
  Print an integer "{:d}".format().
Args:
  value (int): The integer.
Return:
  if typeerror or valueerror - false.
  otherwise true.
"""
def safe_print_integer_err(value):
  try:
    print("{:d}".format(value))
    return (True)
  except (TypeError, ValueError):
    print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
    return False
