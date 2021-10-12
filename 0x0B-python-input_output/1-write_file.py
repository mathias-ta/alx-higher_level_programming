#!/usr/bin/python3
"""
contains method to write to a file
"""


def write_file(filename="", text=""):
    """Write text to filename"""
    with open(filename, mode="w", encoding="utf-8") as f_name:
        return(f_name.write(text))
