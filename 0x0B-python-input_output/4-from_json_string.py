#!/usr/bin/python3
"""Class description and import JSON."""
import json


def from_json_string(my_str):
    """Function to convert a JSON string to python object."""
    y = json.loads(my_str)
    return y
