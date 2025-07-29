#!/usr/bin/python3
"""
Save Object to a file
"""

import json


def save_to_json_file(my_obj, filename):
    """function that writes an Obj to a text file, using a JSON repr
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
