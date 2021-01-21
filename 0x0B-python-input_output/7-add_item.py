#!/usr/bin/python3
"""Class description and import JSON """
from sys import argv
import json
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    new_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    new_list = []
for item in range(1, len(argv)):
    new_list.append(argv[item])
save_to_json_file(new_list, "add_item.json")
