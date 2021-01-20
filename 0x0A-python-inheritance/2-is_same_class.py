#!/usr/bin/python3
"""
Project: 0x0A-python-inheritance
Task: 2
"""


def is_same_class(obj, a_class):
     """True if it is an instance, False otherwise"""

     if type(obj) == a_class:
          return True
     else:
          return False
