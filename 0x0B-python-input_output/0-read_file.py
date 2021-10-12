#!/usr/bin/python3
"""
contains methodto read a file
"""


def read_file(filename=""):
    """Reads a file with filename"""
    new_file = open(filename)
    filetxt = new_file.read()
    new_file.close()
    filetxt
