#!/usr/bin/python3
"""A Class named Mylist inherit from list"""


class MyList(list):
    """Sort the instance list"""
    def print_sorted(self):
        print(sorted(self))
