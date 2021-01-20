#!/usr/bin/python3
"""
Project: 0x0A-python-inheritance.
Task: 6
"""


class BaseGeometry():
    """
    Public instance method: def area(self):
    that raises an Exception with the message area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")
