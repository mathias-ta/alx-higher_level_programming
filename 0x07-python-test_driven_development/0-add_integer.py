#!/usr/bin/python3
"""
Method to add two integers
"""


def add_integer(a, b=98):
    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return a + b
