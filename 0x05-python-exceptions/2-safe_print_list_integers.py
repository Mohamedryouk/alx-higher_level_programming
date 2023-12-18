#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
	try:
		count = 0
		for i in range(x):
			value = my_list[i]
			if isinstance(value, int):
				print("{:d}".format(value), end="")
				count += 1
		print()
	except (ValueError, TypeError, IndexError):
		pass
	return count
