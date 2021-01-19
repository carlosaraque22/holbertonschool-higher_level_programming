#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        l = [i for i in self]
        l.sort()
        print(l)
