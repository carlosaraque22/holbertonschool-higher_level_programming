#!/usr/bin/python3
for lowercases in range(97, 123):
    if lowercases in (101,113):
        continue
    else:
        print("{:c}".format(lowercases), end="")
