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

    def getWidth (self):
        return self.__width
    def getHeight (self):
        return self.__height
    def getX (self):
        return self.__x
    def getY (self):
        return self.__y