#!/usr/bin/python3
"""
Contain function "write_file"
"""


def write_file(filename="", text=""):
    """return the nbr of chars written to "filename" frm "text" """
    with open(filename, 'w', encoding='utf=8') as fl:
        return fl.write(text)
