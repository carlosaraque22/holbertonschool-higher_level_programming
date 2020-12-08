#!/usr/bin/python3
for letters in range(ord('z'), ord('a') - 1, -1):
        print("{:c}".format((letters - 32) if letters % 2 else letters), end='')
