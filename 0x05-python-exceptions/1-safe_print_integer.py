#!/usr/bin/python3
def safe_print_integer(value):
	try:
		value_type = int(value)
		print("{:d}".format(value_type))
		return True
	except (ValueError, TypeError):
		return False