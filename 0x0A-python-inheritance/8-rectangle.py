#!/usr/bin/python3
__import__("7-base_geometry")
"""
contains class called Rectangle that inherits from BaseGeometry
"""


class Rectangle:
    """Inherits from geometry"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
