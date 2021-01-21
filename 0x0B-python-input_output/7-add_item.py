#!/usr/bin/python3
"""Class description and import JSON """
from sys import argv
import json
create_json = __import__('6-load_from_json_file').load_from_json_file
save_json = __import__('5-save_to_json_file').save_to_json_file


try:
    new_list = create_json("add_item.json")
except FileNotFoundError:
    new_list = []
for item in range(1, len(argv)):
    new_list.append(argv[item])
save_json(new_list, "add_item.json")
