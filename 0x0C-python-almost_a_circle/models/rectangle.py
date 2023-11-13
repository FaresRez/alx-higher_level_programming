#!/usr/bin/python3
from base import Base
"""Rectangle class"""


class Rectangle(Base):
    """Rectangle class inherit from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        assert isinstance(width, int), "width must be an integer"
        assert isinstance(height, int), "height must be an integer"
        assert isinstance(x, int), "x must be an integer"
        assert isinstance(y, int), "y must be an integer"
        assert width > 0, "width must be > 0"
        assert height > 0, "height must be > 0"
        assert x >= 0, "x must be >= 0"
        assert y >= 0, "y must be >= 0"

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError(f"height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError(f"x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError(f"y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the area of a rectangle."""
        return self.__height * self.__width
    
    def display(self):
        """Displays the rectangle on screen."""
        # for i in range(self.__height):
        #     for j in range(self.__width):
        #         print("#", end="")
        #     print()
        print('\n'.join(['#' * self.__width for _ in range(self.__height)]))

r1 = Rectangle(4, 6)
r1.display()
print("---")

r1 = Rectangle(2, 2)
r1.display()

