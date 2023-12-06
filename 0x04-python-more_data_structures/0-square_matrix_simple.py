#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    nw_matrix = [[ix ** 2 for ix in rw] for rw in matrix]
    return nw_matrix
