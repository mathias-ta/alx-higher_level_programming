#!/usr/bin/python3
"""
Contains function that
returns dictionary description with simple data structure
"""


def class_to_json(obj):
    """Returns dictionary description with simple data structure"""
    return obj.__dict__
