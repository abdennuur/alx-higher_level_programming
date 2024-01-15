#!/usr/bin/python3
'''module for Base unit tests'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''Test Base class'''

    def setUp(self):
        '''Import module, instantiate class'''
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''Clean up after eny test_method'''
        pass

    def test_A_nb_objects_private(self):
        '''Test if nb_objects -> private class attribute'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_B_nb_objects_initialized(self):
        '''Tests if nb_objects initializes to zero.'''
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)

    def test_C_instantiation(self):
        '''Test Base() instantiation'''
        bs = Base()
        self.assertEqual(str(type(bs)), "<class 'models.base.Base'>")
        self.assertEqual(bs.__dict__, {"id": 1})
        self.assertEqual(bs.id, 1)

    def test_D_constructor(self):
        '''Test the constructor signature'''
        with self.assertRaises(TypeError) as ee:
            Base.__init__()
        mesg = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(ee.exception), mesg)

    def test_D_constructor_args_2(self):
        '''Test the constructor signature with 2 notself args'''
        with self.assertRaises(TypeError) as ee:
            Base.__init__(self, 1, 2)
        mesg = "__init__() takes from 1 to 2 positional arguments but 3 \
were given"
        self.assertEqual(str(ee.exception), mesg)

    def test_E_consecutive_ids(self):
        '''Test the consecutive ids'''
        bs1 = Base()
        bs2 = Base()
        self.assertEqual(bs1.id + 1, bs2.id)

    def test_F_id_synced(self):
        '''Test the sync btwn class and instance id'''
        bs = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), bs.id)

    def test_F_id_synced_more(self):
        '''Test sync btwn class and instance id'''
        bs = Base()
        bs = Base("Foo")
        bs = Base(98)
        bs = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), bs.id)

    def test_G_custom_id_int(self):
        '''Tests custom int id.'''
        ix = 98
        bs = Base(ix)
        self.assertEqual(bs.id, ix)

    def test_G_custom_id_str(self):
        '''Test custom int id'''
        ix = "FooBar"
        bs = Base(ix)
        self.assertEqual(bs.id, ix)

    def test_G_id_keyword(self):
        '''Test id passed as keyword arg'''
        ix = 421
        bs = Base(id=ix)
        self.assertEqual(bs.id, ix)

    # ----------------- Test #15 ------------------------
    def test_H_to_json_string(self):
        '''Test to_json_string() signature'''
        with self.assertRaises(TypeError) as ee:
            Base.to_json_string()
        st = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(ee.exception), st)

        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        d = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{"foobarrooo": 989898}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"foobarrooo": 989898}]')

        d = [{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]
        self.assertEqual(Base.to_json_string(d),
                         '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]')

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(len(Base.to_json_string(d)),
                         len(str(d)))
        d = [{}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}]')
        d = [{}, {}]
        self.assertEqual(Base.to_json_string(d),
                         '[{}, {}]')

        rt1 = Rectangle(10, 7, 2, 8)
        dictionary = rt1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        rt1 = Rectangle(10, 7, 2, 8)
        rt2 = Rectangle(1, 2, 3, 4)
        rt3 = Rectangle(2, 3, 4, 5)
        dictionary = [rt1.to_dictionary(), rt2.to_dictionary(),
                      rt3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        rt1 = Square(10, 7, 2)
        dictionary = rt1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary = str([dictionary])
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

        rt1 = Square(10, 7, 2)
        rt2 = Square(1, 2, 3)
        rt3 = Square(2, 3, 4)
        dictionary = [rt1.to_dictionary(), rt2.to_dictionary(),
                      rt3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)

    # ----------------- Test #17 ------------------------
    def test_H_test_from_json_string(self):
        '''Test to_json_string() signature'''
        with self.assertRaises(TypeError) as ee:
            Base.from_json_string()
        st = "from_json_string() missing 1 required positional argument: \
'json_string'"
        self.assertEqual(str(ee.exception), st)

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

        st = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}, \
{"x": 101, "y": 20123, "width": 312321, "id": 522244, "height": 34340}]'
        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5},
             {'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        self.assertEqual(Base.from_json_string(st), d)

        d = [{}, {}]
        st = '[{}, {}]'
        self.assertEqual(Base.from_json_string(st), d)
        d = [{}]
        st = '[{}]'
        self.assertEqual(Base.from_json_string(st), d)

        d = [{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]
        st = '[{"foobarrooo": 989898}, {"abc": 123}, {"HI": 0}]'
        self.assertEqual(Base.from_json_string(st), d)

        d = [{"foobarrooo": 989898}]
        st = '[{"foobarrooo": 989898}]'
        self.assertEqual(Base.from_json_string(st), d)

        d = [{'x': 1, 'y': 2, 'width': 3, 'id': 4, 'height': 5}]
        st = '[{"x": 1, "y": 2, "width": 3, "id": 4, "height": 5}]'
        self.assertEqual(Base.from_json_string(st), d)

        d = [{'x': 101, 'y': 20123, 'width': 312321, 'id': 522244,
             'height': 34340}]
        st = '[{"x": 101, "y": 20123, "width": 312321, "id": 522244, \
"height": 34340}]'
        self.assertEqual(Base.from_json_string(st), d)

        list_in = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        list_out = Rectangle.from_json_string(
            Rectangle.to_json_string(list_in))
        self.assertEqual(list_in, list_out)

        # ----------------- Test #16 ------------------------
    def test_I_save_to_file(self):
        '''Tests save_to_file() method.'''
        import os
        rt1 = Rectangle(10, 7, 2, 8)
        rt2 = Rectangle(2, 4)
        Rectangle.save_to_file([rt1, rt2])

        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 105)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Rectangle.json")
        except:
            pass
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        rt2 = Rectangle(2, 4)
        Rectangle.save_to_file([rt2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(len(file.read()), 52)

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except:
            pass
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        rt2 = Square(1)
        Square.save_to_file([rt2])
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 38)

        # ----------------- Tests for #18 ------------------------
    def test_J_create(self):
        '''Tests create() method.'''
        rt1 = Rectangle(3, 5, 1)
        rt1_dictionary = rt1.to_dictionary()
        rt2 = Rectangle.create(**rt1_dictionary)
        self.assertEqual(str(rt1), str(rt2))
        self.assertFalse(rt1 is rt2)
        self.assertFalse(rt1 == rt2)

        # ----------------- Test #19 ------------------------
    def test_K_load_from_file(self):
        '''Test load_from_file() method'''
        rt1 = Rectangle(10, 7, 2, 8)
        rt2 = Rectangle(2, 4)
        list_in = [rt1, rt2]
        Rectangle.save_to_file(list_in)
        list_out = Rectangle.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_in = [s1, s2]
        Square.save_to_file(list_in)
        list_out = Square.load_from_file()
        self.assertNotEqual(id(list_in[0]), id(list_out[0]))
        self.assertEqual(str(list_in[0]), str(list_out[0]))
        self.assertNotEqual(id(list_in[1]), id(list_out[1]))
        self.assertEqual(str(list_in[1]), str(list_out[1]))

if __name__ == "__main__":
    unittest.main()
