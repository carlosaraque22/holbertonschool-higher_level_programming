#!/usr/bin/python3
""" Class description """


def write_file(filename="", text=""):
    """ Write a string into a text file (UTF8) """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)