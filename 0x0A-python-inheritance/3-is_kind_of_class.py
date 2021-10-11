#!/usr/bin/python3
"""
Contain method called is_kind_of_class
that check object for instance of a class called a_class or
a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """Check obj for a_class"""
    return isinstance(obj) == a_class
