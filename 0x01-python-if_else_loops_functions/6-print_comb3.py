#!/usr/bin/python3
for num in range(10):
    for numb in range(num + 1, 10):
        print("{:d}{:d}".format(num, numb),end=',' if (num, numb) != (8, 9) else "")
