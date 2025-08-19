#!/usr/bin/python3
"""Defines the Rectangle class that inherits from Base."""


from models.base import Base


class Rectangle(Base):
    """Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def setters_validation(self, value, name):
        """Validate an attribute value.

            Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0 for width/height or < 0 for x/y.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if name in ["width", "height"] and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if name in ["x", "y"] and value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.setters_validation(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.setters_validation(value, "height")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.setters_validation(value, "x")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.setters_validation(value, "y")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle using the '#' character."""
        for _ in range(self.height):
            print("#" * self.width)
