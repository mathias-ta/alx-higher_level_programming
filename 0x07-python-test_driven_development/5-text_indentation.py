#!/usr/bin/python3
"""
Print two new line after each period(.)
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("taxt must be a string")
    for char in text:
        if ord(char) == ord(".") or ord(char) == ord("?") or ord(char) == ord(":"):
            print(char)
            print("")
        else:
            print(char, end="")
