#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [] 
    if matrix is not None:
        for i in matrix:
            square = lambda j: j ** 2
            new_matrix.append(list(map(square, i)))
        return new_matrix
    return None
