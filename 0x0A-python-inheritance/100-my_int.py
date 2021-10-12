#!/usr/bin/python3
"""
Contains class called MyInt inherits from int
"""


class MyInt(int):
    """Inherits from int"""
    def __init__(self, obj):
        self.__obj = obj

    def __eq__(self, obj1):
        return self.__obj != obj1

    def __ne__(self, obj1):
        return self.__obj == obj1

