#!/usr/bin/python3
""" Class description and import JSON """
import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file in JSON format """
    with open(filename, encoding='utf-8', mode='w') as my_file:
        my_file.write(json.dumps(my_obj))
