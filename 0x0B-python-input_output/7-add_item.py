#!/usr/bin/python3
"""
this program convert to JSON object string
"""
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


list = []
if len(sys.argv) > 1:
    for item in sys.argv[1:]:
        list.append(item)
save_to_json_file(list, "add_item.json")
load_from_json_file("add_item.json")
