#!/usr/bin/python3
'''Module for the Square class'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''the Square class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''the constructor.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Return str info about the square'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Size of the square'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''internal method to update instance attributes via */**args'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Update the instance attributes via no-keyword & keyword args'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Return dictionary representation of the class'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
