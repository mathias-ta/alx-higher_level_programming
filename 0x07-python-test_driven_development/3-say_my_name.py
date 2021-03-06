#!/usr/bin/python3
"""
Print my name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {:s} {:s}".format(first_name, last_name))
    else:
        if not isinstance(first_name, str):
            raise TypeError("first_name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("last_name must be a string")
