#!/usr/bin/python3
"""
contains class student and method to retrieves
a dictionary representation of attributes of student
"""


class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            dicts = {}
            for i in attrs:
                if i in self.__dict__.keys():
                    dicts[i] = self.__dict__[i]
            return dicts
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for j, k in json.items():
            setattr(self, j, k)
