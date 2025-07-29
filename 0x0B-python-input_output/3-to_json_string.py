#!/usr/bin/python3
"""
To JSON string
"""

import json


def to_json_string(my_obj):
    return json.dumps(my_obj, default=lambda obj: obj.__dict__)
