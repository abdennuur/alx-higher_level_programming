#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nd = {ix: (a_dictionary[ix] * 2) for ix in a_dictionary}
    return nd
