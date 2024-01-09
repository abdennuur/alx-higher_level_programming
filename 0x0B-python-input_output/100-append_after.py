#!/usr/bin/python3
"""
Contain append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """append new_string after a line containing
    "search_string" in "filename" """
    with open(filename, 'r', encoding='utf-8') as fl:
        line_ls = []
        while True:
            line = fl.readline()
            if line == "":
                break
            line_ls.append(line)
            if search_string in line:
                line_ls.append(new_string)
    with open(filename, 'w', encoding='utf-8') as fl:
        fl.writelines(line_ls)
