#!/usr/bin/python3
"""
Contain method callwd is_same_class
that check object for instance of a class called a_class
"""


def is_same_class(obj, a_class):
    """Check obj for a_class"""
    return type(obj) == a_class
