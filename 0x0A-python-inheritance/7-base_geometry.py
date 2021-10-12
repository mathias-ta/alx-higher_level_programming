#!/usr/bin/python3
"""
Contains class called BaseGeometry which contains methods
called area and integer_validator
"""


class BaseGeometry():
    """
    Contains methods area and integer_validator
    """
    def area(self):
        """area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate value
        """
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
