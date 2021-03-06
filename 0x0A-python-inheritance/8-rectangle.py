#!/usr/bin/python3
"""
contains class called Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from geometry"""
    def __init__(self, width, height):
        """
        Validate and initialize width and height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
