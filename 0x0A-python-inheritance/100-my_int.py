#!/usr/bin/python3
"""class BaseGeometry"""


class MyInt(int):
    """class MyInt that inherits from int"""
    def __eq__(self, other):
        """inverted equality"""
        return super().__ne__(other)

    def __ne__(self, other):
        """inverted inequality"""
        return super().__eq__(other)
