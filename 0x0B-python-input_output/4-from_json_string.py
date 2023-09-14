#!/usr/bin/python3
"""
this program convert from a JSON object string
"""


import json


def from_json_string(my_obj):
    """
    thid function return a string from JSON object
    """
    return json.loads(my_obj)
