#!/usr/bin/python3
"""
Contain class Student
"""


class Student:
    """Representation of student"""
    def __init__(self, first_name, last_name, age):
        """Initialize the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return dictionary representation of Student instance
        with specified attribute"""
        if attrs is None:
            return self.__dict__
        nw_dict = {}
        for i in attrs:
            try:
                nw_dict[i] = self.__dict__[i]
            except FileNotFoundError:
                pass
        return nw_dict

    def reload_from_json(self, json):
        """replace all attributes of Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
