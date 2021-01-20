#!/usr/bin/python3
"""
Project: 0x0A-python-inheritance
Task: 3
"""


def is_kind_of_class(obj, a_class):
    """True if it is, False otherwise"""

    if issubclass(type(obj), a_class):
        return True
    return False
