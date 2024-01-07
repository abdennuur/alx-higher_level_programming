#!/usr/bin/python3
"""
This is "5-test_indentation"i module
5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """split a txt into lines along "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flg = 0
    for ax in text:
        if flg == 0:
            if ax == ' ':
                continue
            else:
                flg = 1
        if flg == 1:
            if ax == '?' or ax == '.' or ax == ':':
                print(ax)
                print()
                flg = 0
            else:
                print(ax, end="")
