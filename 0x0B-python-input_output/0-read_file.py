#!/usr/bin/python3
""" Class declaration"""


def read_file(filename=""):
    """
    Function that reads a file (UTF8) and prints it
    """
    with open(filename, encoding='utf-8') as a_file:
        print a_file.read(), end="")