#!/usr/bin/python3
"""
Contain class MyInt
"""


class MyInt(int):
    """rebel version of integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """create new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is  =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is  !="""
        return int(self) == other
