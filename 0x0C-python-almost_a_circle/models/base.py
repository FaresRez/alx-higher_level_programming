#!/usr/bin/python3
import json
"""The class Base that handle id"""


class Base:
    """Base class

        Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instances."""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
