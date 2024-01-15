#!/usr/bin/python3
'''module for a Base class'''
from json import dumps, loads
import csv


class Base:
    '''representation of base of OOP hierarchy.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''the Constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Jsonifies dictionary so -> quite rightly and longer'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''Unjsonifies -> dictionary.'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Save jsonified object to file'''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        '''Load instance frm dictionary'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            nw = Rectangle(1, 1)
        elif cls is Square:
            nw = Square(1)
        else:
            nw = None
        nw.update(**dictionary)
        return nw

    @classmethod
    def load_from_file(cls):
        '''Load str frm file and unjsonifies'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as fl:
            return [cls.create(**d) for d in cls.from_json_string(fl.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Save object to a csv file'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Load object to a csv file'''
        from models.rectangle import Rectangle
        from models.square import Square
        rt = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as fl:
            reader = csv.reader(fl)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                rt.append(cls.create(**d))
        return rt

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for ix in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((ix.x + t.pos()[0], ix.y - t.pos()[1]))
            t.pensize(10)
            t.forward(ix.width)
            t.left(90)
            t.forward(ix.height)
            t.left(90)
            t.forward(ix.width)
            t.left(90)
            t.forward(ix.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
