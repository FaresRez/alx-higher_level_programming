#!/usr/bin/python3
"""
    this program write in a file
"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as f:
        nb = f.write(text)
        f.close()
        return (nb)
