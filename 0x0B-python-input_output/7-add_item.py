#!/usr/bin/python3
"""
Load, add, save
"""


if __name__ == "__main__":
    import sys
    import importlib
    import json

    save_to_json_file = importlib.import_module('5-save_to_json_file')\
        .save_to_json_file
    load_from_json_file = importlib.import_module('6-load_from_json_file')\
        .load_from_json_file

    my_list = list(load_from_json_file("add_item.json"))

    my_list.extend(sys.argv[1:])
    save_to_json_file(my_list, "add_item.json")
