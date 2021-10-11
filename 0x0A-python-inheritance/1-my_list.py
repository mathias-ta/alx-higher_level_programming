#!/usr/bin/python3
"""
contains cass called MyList that inherits list and
a method called print_sorted to print ascending sorted list
"""


class MyList(list):
    """
    class inherit list
    """
    def print_sorted(self):
        """
        method to print sorted list
        """
        print(sorted(self))
