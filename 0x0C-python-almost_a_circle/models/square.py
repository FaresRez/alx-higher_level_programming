#!/usr/bin/python3
from rectangle import Rectangle
"""Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherit from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the square."""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}'

    @property
    def size(self):
        """Return the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

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
            attribut_list = ['id', 'size', 'x', 'y']
            for attribut, arg in zip(attribut_list, args):
                setattr(self, attribut, arg)

    def to_dictionary(self):
        """Return a dictionary with all the object's attributes."""
        return {"id": getattr(self, "id"),
                "size": getattr(self, "size"),
                "x": getattr(self, "x"),
                "y": getattr(self, "y")}
