#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""
contains class called Rectangle that inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """Inherits from geometry"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
