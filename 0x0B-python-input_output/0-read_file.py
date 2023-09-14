#!/usr/bin/python3
"""
    the program read files
"""


def read_file(filename=""):
    """
        read a given file
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read())
        f.close()
