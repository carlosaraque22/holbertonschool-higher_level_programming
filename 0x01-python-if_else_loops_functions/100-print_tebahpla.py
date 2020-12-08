#!/usr/bin/python3
for letts in range(ord("z"), ord("a") - 1, -1):
        print("{:c}".format((letts - 32) if letts % 2 else letts), end="")
