#!/usr/bin/python3
"""Module with class Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of a square"""
    def __init__(self, size):
        """Instantiation of a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of a square"""
        return (self.__size ** 2)