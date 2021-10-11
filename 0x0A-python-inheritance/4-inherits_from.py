#!/usr/bin/python3
"""
Contain method called inherit_from
that returns True if the object is an instance of a class
that inherited (directly or indirectly)
from the specified class ; otherwise False
"""


def inherit_from(obj, a_class):
    """Check obj for a_class"""
    return (type(onj) is not a_class and issubclass(obj, a_class))
