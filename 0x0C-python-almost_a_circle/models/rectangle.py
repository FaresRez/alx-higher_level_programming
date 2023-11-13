#!/usr/bin/python3
from base import Base
""""""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def Width(self):
        return self.__width

    @Width.setter
    def Width(self, value):
        if not isinstance(value, int):
            raise TypeError(f"width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def Height(self):
        return self.__height

    @Height.setter
    def Height(self, value):
        if not isinstance(value, int):
            raise TypeError(f"height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def X(self):
        return self.__x

    @X.setter
    def X(self, value):
        if not isinstance(value, int):
            raise TypeError(f"x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def Y(self):
        return self.__y

    @Y.setter
    def Y(self, value):
        if not isinstance(value, int):
            raise TypeError(f"y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value


try:
    Rectangle(10, "2")
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r = Rectangle(10, 2)
    r.width = -10
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r = Rectangle(10, 2)
    r.x = {}
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    Rectangle(10, 2, 3, -1)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
