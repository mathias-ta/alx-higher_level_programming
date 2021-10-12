#!/usr/bin/python3
"""
contains class called square that inherits from Rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Inherits from geometry"""
    def __init__(self, size):
        """
        Validate and initialize width and height
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
