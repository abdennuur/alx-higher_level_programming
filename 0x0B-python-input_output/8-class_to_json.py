#!/usr/bin/python3
"""
Contain "class_to_json" function
"""


def class_to_json(obj):
    """return dictionary description with a simple data structure
    (list, dictionary, str, int and bool)
    for JSON serialization of object"""
    return obj.__dict__
