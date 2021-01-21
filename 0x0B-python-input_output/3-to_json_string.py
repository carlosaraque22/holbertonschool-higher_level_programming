#!/usr/bin/python3
""" Class description and import JSON"""
import json


def to_json_string(my_obj): 
    """ Function to convert a python object to JSON string """
    y = json.dumps(my_obj)
    return y
