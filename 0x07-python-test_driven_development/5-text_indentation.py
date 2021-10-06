#!/usr/bin/python3
"""
Print two new line after each period(.)
"""


def text_indentation(text):
    """
    Print separated string after '.', '?' and ':'
    """
    ch_char = "a"
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if (ord(char) == ord(".") or ord(char) == ord("?") or
                ord(char) == ord(":")):
            ch_char = char
            print(char)
            print("")
        elif ((ord(ch_char) == ord(".") or ord(ch_char) == ord("?") or
                ord(ch_char) == ord(":")) and ord(char) == ord(" ")):
            if ord(ch_char) != ord("a"):
                ch_char = "a"
        else:
            ch_char = "a"
            print(char, end="")
# text_indentation("Holberton. School? Jhon")
