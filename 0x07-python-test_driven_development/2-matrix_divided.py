#!/usr/bin/python3
"""
Divide each elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix i.e matrix/div
    """
    new_matrix = []
    print_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(print_msg)
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if type(i) is not list:
            raise TypeError(print_msg)
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        k = []
        for j in i:
            if not isinstance(j, (float, int)):
                raise TypeError(print_msg)
            k.append(round(j / div, 2))
        new_matrix.append(k)
    return new_matrix
