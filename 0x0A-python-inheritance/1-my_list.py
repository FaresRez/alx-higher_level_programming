#!/usr/bin/python3
"""
    1-my_list.py: class Mylist
"""
class MyList(list):
    """
        Mylist class inherit from list class
        Attributes:
        Modules:
            print_sorted: print the the sorted list
    """
    def print_sorted(self):
        """
            print_sorted: print the the sorted list
        """
        l = sorted(self)
        print(l)
