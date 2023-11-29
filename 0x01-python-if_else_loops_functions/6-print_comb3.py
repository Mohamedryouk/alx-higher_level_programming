#!/usr/bin/python3
for num in range(10):
    for numb in range(num + 1, 10):
        output = "{:d}{:d}".format(num, numb)
        print(output,end=", " if (num, numb) != (8, 9) else "\n")
