#!/usr/bin/python3
"""
    0-lookup: lookup()
"""
def lookup(obj):
    """
        return the list of available attributes and methods of an object
        Args:
            obj: object
    """
    return (dir(obj))
