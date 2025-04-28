#!/usr/bin/python3

"""Define a class square"""


class Square:
    """define a private attribute size"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self._position = position

    def area(self):
        return self._size ** 2

    @property
    def size(self):
        return self._size

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        if (not isinstance(self._position, tuple) or self._position[0] < 0
                or self._position[1] < 0 or len(self._position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    @size.setter
    def size(self, value):
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self._size = value

    def my_print(self):
        if self._size == 0:
            print()
        else:
            for i in range(self._size):
                if self._position[1] <= 0:
                    print(" " * self._position[0], end="")
                for j in range(self._size):
                    print("#", end="")
                print()
