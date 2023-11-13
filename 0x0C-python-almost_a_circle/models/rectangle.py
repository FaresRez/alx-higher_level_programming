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
    def Width (self):
        return self.__width
    
    @Width.setter
    def Width (self, value):
        if isinstance(value, int):
            self.__width = value
        else:
            raise 
    
    @property
    def Height (self):
        return self.__height
    
    @Height.setter
    def Height (self, value):
        self.__height = value

    @property
    def X (self):
        return self.__x
    
    @X.setter
    def X (self, value):
        self.__x = value
    
    @property
    def Y (self):
        return self.__y

    @Y.setter
    def Y (self, value):
        self.__y = value
        

    
    
