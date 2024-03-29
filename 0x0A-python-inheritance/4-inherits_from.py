#!/usr/bin/python3
"""returns True if the object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """return true or false"""
    return isinstance(obj, a_class) and type(obj) != a_class
