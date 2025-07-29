#!/usr/bin/python3
"""
From JSON string to Object
"""

import json


def from_json_string(my_str):
    """function that returns the object (string) from a JSON representation
    """
    return json.loads(my_str)
