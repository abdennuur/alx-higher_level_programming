#!/usr/bin/python3
"""
module contain the function is_same_class
"""


def is_same_class(obj, a_class):
    """return true -> obj is the exact class a_class, -> false"""
    return (type(obj) == a_class)
