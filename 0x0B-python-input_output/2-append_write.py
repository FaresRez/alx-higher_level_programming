#!/usr/bin/python3
"""
    this program append in a file
"""


def append_write(filename="", text=""):
    """
        this function append to a file and return the nb of char added
    """
    with open(filename, 'a', encoding='utf-8') as f:
        nb = f.write(text)
        return (nb)
