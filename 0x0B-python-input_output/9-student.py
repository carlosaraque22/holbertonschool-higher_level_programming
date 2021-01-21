#!/usr/bin/python3
""" Class description """


class Student:
    """ Class named student """


    def __init__(self, first_name, last_name, age):
        """ constructor """


        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        """ Return a dictionary of student """
        return self.__dict__
