#!/usr/bin/python3
"""
Contain method called inherits_from
that returns True if the object is an instance of a class
that inherited (directly or indirectly)
from the specified class ; otherwise False
"""


def inherits_from(obj, a_class):
    """Check obj for a_class
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
