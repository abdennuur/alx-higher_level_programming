#!/usr/bin/python3
"""define the function to scalar divide the matrix"""


def matrix_divided(matrix, div):
    """divide matrix by scalar int, rounded to 2 dcml places"""
    import decimal
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(err_msg)
    len_r = []
    row_c = 0
    for rw in matrix:
        if type(rw) is not list:
            raise TypeError(err_msg)
        len_r.append(len(rw))
        for elmnt in rw:
            if type(elmnt) not in [int, float]:
                raise TypeError(err_msg)
        row_c += 1
    if len(set(len_r)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if int(div) == 0:
        raise ZeroDivisionError("division by zero")
    nw_matrix = list(map(lambda rw:
                          list(map(lambda ix: round(ix/div, 2), rw)), matrix))
    return nw_matrix
