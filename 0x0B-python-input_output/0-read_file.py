#!/usr/bin/python3
"""
contains methodto read a file
"""


def read_file(filename=""):
    """Reads a file with filename"""
    new_file = open(filename, mode="r", encoding="utf-8")
    filetxt = new_file.read()
    new_file.close()
    filetxt
