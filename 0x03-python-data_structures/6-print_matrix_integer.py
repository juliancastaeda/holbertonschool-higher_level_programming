#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for k in range(len(matrix)):
        for j in range(len(matrix[k])):
            if (j < len(matrix[k])) - 1:
                print('{:d}'.format(matrix[k][j]), end='')
            else:
                print('{:d}'.format(matrix[k][j]), end='')
        print()        
