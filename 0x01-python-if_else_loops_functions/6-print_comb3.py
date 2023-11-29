#!/usr/bin/python3
for num in range(0, 9):
    for numb in range(num + 1, 10):
        if (num, numb) == (8, 9):
            print("{:d}{:d}".format(num, numb))
        else:
            print("{:d}{:d}".format(num, numb), end=", ")
