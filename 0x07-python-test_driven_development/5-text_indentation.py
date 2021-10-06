#!/usr/bin/python3
"""
Print two new line after each period(.)
"""


def text_indentation(text):
    """
    Print separated string after '.', '?' and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if (ord(char) == ord(".") or ord(char) == ord("?") or
                ord(char) == ord(":")):
            print(char)
            print("")
        else:
            print(char, end="")
text_indentation(None)
