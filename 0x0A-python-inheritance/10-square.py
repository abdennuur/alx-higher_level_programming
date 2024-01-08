#!/usr/bin/python3
"""
Contain  class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """representation square"""
    def __init__(self, size):
        """instantiation of square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"return area of square"""
        return self.__size ** 2
