#!/usr/bin/python3
"""
this program write to a text file to a file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    this function write a JSON obj to a file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
