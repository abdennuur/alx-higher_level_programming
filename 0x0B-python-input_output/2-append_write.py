#!/usr/bin/python3
"""
function to appends a str
"""


def append_write(filename="", text=""):
    """return nbr of chars added:"""
    with open(filename, 'a', encoding='utf=8') as fl:
        return fl.write(text)
