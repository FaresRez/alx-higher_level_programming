#!/usr/bin/python3
"""
    an empty Rectangle class
"""


class Rectangle:
    """
        Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ""
        a = [str(self.print_symbol) * self._width for _ in range(self._height)]
        return "\n".join(a)

    def __repr__(self):
        return f"Rectangle({self._width}, {self._height})"

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    def area(self):
        return self._width * self._height

    def perimeter(self):
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width + self._height) * 2

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
