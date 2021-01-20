#!/usr/bin/python3
"""
Project: 0x0A-python-inheritance.
Task: 4
"""


def inherits_from(obj, a_class):
    """True if it is, False otherwise"""

    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    return False
