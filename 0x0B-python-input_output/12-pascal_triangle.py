#!/usr/bin/python3
"""
Contains method to create a pascal triangle
"""


def pascal_triangle(n):
    """returns pascal triangle"""
    ps_t = [[1]]

    if n <= 0:
        return []
    if n == 1:
        return ps_t
    else:
        for i in range(n-1):
            ps_t.append([a+b for a, b in zip([0] + ps_t[-1], ps_t[-1] + [0])])
        return ps_t
