#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if ord(i) == 65 or ord(i) == 71:
        print("", end="")
    else:
        print("{:c}".format(i), end="")
