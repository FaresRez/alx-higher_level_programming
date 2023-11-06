#!/usr/bin/python3
"""function that return a list of available attributes and methods"""


def lookup(obj):
    """return a list of available attributes and methods"""
    return dir(obj)
