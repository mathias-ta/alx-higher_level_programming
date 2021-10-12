#!/usr/bin/python3
"""
contains method to append to a file
"""


def append_write(filename="", text=""):
    """Append text to filename"""
    with open(filename, mode="a", encoding="utf-8") as f_name:
        return(f_name.write(text))
