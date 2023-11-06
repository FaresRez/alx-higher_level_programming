#!/usr/bin/python3
"""return true if the object is an instance of the specified class"""


def inherits_from(obj, a_class):
    """Verifiying is the instance beyong to a specific class or not"""
    return isinstance(obj, a_class)


a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))