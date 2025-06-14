#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """empty class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
            self.integer_validator("height", height)
            self.integer_validator("width", width)
            self._height = height
            self._width = width
