#!/usr/bin/python3
"""
Contains class Base which contains
private class attribute __nb_objects and class constructor __init__
"""


import json


class Base():
    """
    contains
    class attribute __nb_objects
    methods __init__(self, id=None)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """retern json representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json string into a file"""
        objs = []
        if list_objs is not None:
            for obj in list_objs:
                objs.append(cls.to_dictionary(obj))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """return python object of a json string"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            attr = cls(1)
        if cls.__name__ == "Rectangle":
            attr = cls(1, 1)
        attr.update(**dictionary)
        return attr

    @classmethod
    def load_from_file(cls):
        """returns list of instances"""
        file_name = cls.__name__ + ".json"
        list_inst = []
        try:
            withh open(file_name, "r") as f:
                instances = cls.from_json_string(f.read())
            for i, j in enumerate(instances):
                list_inst.append(cls.create(**instances[i]))
        except:
            pass
        return list_inst
