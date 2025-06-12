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

    def area(self):
        """returns the area of the rectangle"""
        return self._height * self._width

    def __str__(self):
        return f"[Rectangle] {self._width}/{self._height}"


class Square(Rectangle):
    """class square that inherits from Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self._size = size
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self._width}/{self._height}"
