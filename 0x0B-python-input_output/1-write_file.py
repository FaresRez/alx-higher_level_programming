#!/usr/bin/python3
"""
write in a file.
"""


def write_file(filename="", text=""):
    """
    Function that return nb of caracters written i a file
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
    