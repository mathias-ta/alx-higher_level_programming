#!/usr/bin/python3
"""
Contains class Base which contains
private class attribute __nb_objects and class constructor __init__
"""

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
