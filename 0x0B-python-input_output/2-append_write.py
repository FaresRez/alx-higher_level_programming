#!/usr/bin/python3
"""
append in a file
"""


def append_write(filename="", text=""):
    """
    function that append in a file
    """
    with open(filename, "a+", encoding="utf-8") as f:
        f.write(text)
    return len(text)
