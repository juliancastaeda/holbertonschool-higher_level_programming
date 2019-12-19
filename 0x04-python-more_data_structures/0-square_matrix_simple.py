#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    if len(matrix) == 0:
        return None
    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda j: j ** 2, matrix[i]))
    return new_matrix
