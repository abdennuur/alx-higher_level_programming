#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ix in matrix:
        print(" ".join("{:d}".format(ji) for ji in ix))
