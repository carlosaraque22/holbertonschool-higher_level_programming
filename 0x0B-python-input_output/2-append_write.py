#!/usr/bin/python3
""" Class description """


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of 
    a text file (UTF8)
    """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return my_file.write(text)
