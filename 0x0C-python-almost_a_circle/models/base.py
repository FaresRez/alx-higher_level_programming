#!/usr/bin/python3
import json
"""The class Base that handle id"""


class Base:
    """Base class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is None:
           Base.__nb_objects+=1
           self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a JSON from a list of dict"""
        return json.dumps([x for x in list_dictionaries])
    
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Save the JSON obj into file
        
            Args:
                list_obj (List[dict]): List of dictionnary object
        """
        if list_objs is None:
            list_objs = []
        with open(f'{cls.__name__}.json',mode="w", encoding="utf-8") as f:
            obj_dict = [obj.to_dictionary() for obj in list_objs]
            f.write(cls.to_json_string(obj_dict))
    
    @staticmethod
    def from_json_string(json_string):
        """Create a string representation from a string JSON

            Args:
                json_string (str): The JSON string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance of this class from dictionary"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        cls.update(new, **dictionary)
        return new
    
    @classmethod
    def load_from_file(cls):
        """Load all objects from file and returns them as a list"""
        try:
            with open(f'{cls.__name__}.json',mode="r", encoding="utf-8") as f:
                list_dict = Base.from_json_string(f.read())
                return [cls.create(**di) for di in list_dict]
        except FileNotFoundError as e:
            return []




            





