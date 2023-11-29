#!/usr/bin/python3
for num in range(0, 100):
    print("{0:02d}{1}".format(int(num), ',' if num < 99 else ''), end=" ")
