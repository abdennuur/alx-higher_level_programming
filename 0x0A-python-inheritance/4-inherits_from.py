#!/usr/bin/python3

"""Define inherited class-checking function"""


def inherits_from(obj, a_class):
    """Checks if object is inherited instance of class.

    Args:
        obj (any): The object to check.
        a_class (type): class to match type of obj to.
    Returns:
        -> obj is an inherited instance of a_class - True.
        Otherwise -> False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
