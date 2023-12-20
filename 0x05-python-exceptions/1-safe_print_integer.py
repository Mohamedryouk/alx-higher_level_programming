#!/usr/bin/python3
def safe_print_integer(value):
	"""	
		Print an integer "{:d}".format().
	Args:
			value (int): The integer.
	Return:
			if typeerror or valueerror - false.
			otherwise true.
	"""	
	try:
		print("{:d}".format(value))
		return (True)
	except (ValueError, TypeError):
		return (False)
