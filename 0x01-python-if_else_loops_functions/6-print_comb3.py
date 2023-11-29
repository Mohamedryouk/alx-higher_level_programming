#!/usr/bin/python3
for num in range (10):
    for numb in range (num + 1, 10):
        print("{:d}{:d}".format(num, numb, ',' if numb < 9 else "\n"), end="")
