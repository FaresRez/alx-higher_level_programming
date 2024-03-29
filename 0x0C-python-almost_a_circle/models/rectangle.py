#!/usr/bin/python3
from base import Base
"""Rectangle class"""


class Rectangle(Base):
    """Rectangle class inherit from Base

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
    """

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

    def __repr__(self) -> str:
        """representation of the object"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"

    @property
    def width(self):
        """width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set new width for rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set new height for rectangle"""
        if not isinstance(value, int):
            raise TypeError(f"height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """position on X axis"""
        return self.__x

    @x.setter
    def x(self, value):
        """set position on X axis"""
        if not isinstance(value, int):
            raise TypeError(f"x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """position on Y axis"""
        return self.__y

    @y.setter
    def y(self, value):
        """set position on Y axis"""
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
        espace = ""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """Update rectangle's attributes (if possible).

            Args:
            *args (ints): New attribute values.
                1st argument represents id attribute
                2nd argument represents width attribute
                3rd argument represent height attribute
                4th argument represents x attribute
                5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args == ():
            for key, arg in kwargs.items():
                setattr(self, key, arg)
        else:
            attribut_list = ['id', 'width', 'height', 'x', 'y']
            for attribut, arg in zip(attribut_list, args):
                setattr(self, attribut, arg)

    def to_dictionary(self):
        """Return a dictionary with all the object's attributes."""
        return {"id": getattr(self, "id"),
                "width": getattr(self, "width"),
                "height": getattr(self, "height"),
                "x": getattr(self, "x"),
                "y": getattr(self, "y")}
