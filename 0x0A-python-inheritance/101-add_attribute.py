#!/usr/bin/python3
"""
Contains a method to add new attribute to an object
"""


def add_attribute(obj, attr, value):
    """Add an attribute"""
    if "__dict__" in dir(obj):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
