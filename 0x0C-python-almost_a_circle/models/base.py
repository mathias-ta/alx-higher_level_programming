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
        return json.dump(list_dictionaries)
