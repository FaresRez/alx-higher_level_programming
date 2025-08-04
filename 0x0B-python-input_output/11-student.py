#!/usr/bin/python3
"""Student to disk and reload"""


class Student:
    """A student Class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None and isinstance(attrs, list) and \
           all(isinstance(key, str) for key in attrs):
            return {
                key: self.__dict__[key]
                for key in attrs
                if key in self.__dict__
            }
        else:
            return self.__dict__


def reload_from_json(self, json):
    return self.__dict__.update(json)
