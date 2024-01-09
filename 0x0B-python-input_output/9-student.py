#!/usr/bin/python3
"""
Contain class "Student"
"""


class Student:
    """Representation of student"""
    def __init__(self, first_name, last_name, age):
        """Initialize student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """return dictionary representation of Student instance"""
        return self.__dict__
