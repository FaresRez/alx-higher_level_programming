#!/usr/bin/python3

"""Define a class square"""


class Square:
    """define a private attribute size"""
    def __init__(self, size=0):
        if (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
