#!/usr/bin/python3
"""
this program create an object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    this function create an object from a JSON file
    """
    with open(filename, encoding='utf-8') as f:
        return json.loads(f.read())
