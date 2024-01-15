#!/usr/bin/python3
'''Module for the  Square unit tests'''
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    '''Test the Base class'''

    def setUp(self):
        '''Import the module,instantiate class'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Clean up after each test_method'''
        pass

    # ----------------- Test #2 ------------------------

    def test_A_class(self):
        '''Test Square class type'''
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def test_B_inheritance(self):
        '''Test if Square -> inherits Base'''
        self.assertTrue(issubclass(Square, Base))

    def test_C_constructor_no_args(self):
        '''Test constructor signature'''
        with self.assertRaises(TypeError) as ee:
            rt = Square()
        s = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(ee.exception), s)

    def test_C_constructor_many_args(self):
        '''Test constructor signature'''
        with self.assertRaises(TypeError) as ee:
            rt = Square(1, 2, 3, 4, 5)
        s = "__init__() takes from 2 to 5 positional arguments but 6 \
were given"
        self.assertEqual(str(ee.exception), s)

    def test_D_instantiation(self):
        '''Tests instantiation.'''
        rt = Square(10)
        self.assertEqual(str(type(rt)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(rt, Base))
        d = {'_Rectangle__height': 10, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(rt.__dict__, d)

        with self.assertRaises(TypeError) as ee:
            rt = Square("1")
        mesg = "width must be an integer"
        self.assertEqual(str(ee.exception), mesg)

        with self.assertRaises(TypeError) as ee:
            rt = Square(1, "2")
        mesg = "x must be an integer"
        self.assertEqual(str(ee.exception), mesg)

        with self.assertRaises(TypeError) as ee:
            rt = Square(1, 2, "3")
        mesg = "y must be an integer"
        self.assertEqual(str(ee.exception), mesg)

        with self.assertRaises(ValueError) as ee:
            rt = Square(-1)
        mesg = "width must be > 0"
        self.assertEqual(str(ee.exception), mesg)

        with self.assertRaises(ValueError) as ee:
            rt = Square(1, -2)
        mesg = "x must be >= 0"
        self.assertEqual(str(ee.exception), mesg)

        with self.assertRaises(ValueError) as ee:
            rt = Square(1, 2, -3)
        mesg = "y must be >= 0"
        self.assertEqual(str(ee.exception), mesg)

        with self.assertRaises(ValueError) as ee:
            rt = Square(0)
        mesg = "width must be > 0"
        self.assertEqual(str(ee.exception), mesg)

    def test_D_instantiation_positional(self):
        '''Test the  positional instantiation'''
        rt = Square(5, 10, 15)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 1}
        self.assertEqual(rt.__dict__, d)

        rt = Square(5, 10, 15, 20)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 20}
        self.assertEqual(rt.__dict__, d)

    def test_D_instantiation_keyword(self):
        '''Test the positional instantiation'''
        rt = Square(100, id=421, y=99, x=101)
        d = {'_Rectangle__height': 100, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(rt.__dict__, d)

    def test_E_id_inherited(self):
        '''Test if id inherited frm Base'''
        Base._Base__nb_objects = 98
        rt = Square(2)
        self.assertEqual(rt.id, 99)

    def test_F_properties(self):
        '''Test property getters/setters'''
        rt = Square(5, 9)
        rt.size = 98
        rt.x = 102
        rt.y = 103
        d = {'_Rectangle__height': 98, '_Rectangle__width': 98,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(rt.__dict__, d)
        self.assertEqual(rt.size, 98)
        self.assertEqual(rt.x, 102)
        self.assertEqual(rt.y, 103)

    # ----------------- Test #3 ------------------------

    def invalid_types(self):
        '''Return tuple of types for validation'''
        t = (3.14, -1.1, float('inf'), float('-inf'), True, "str", (2,),
             [4], {5}, {6: 7}, None)
        return t

    def test_G_validate_type(self):
        '''Test property validation'''
        rt = Square(1)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be an integer".format(attribute)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as ee:
                    setattr(rt, attribute, invalid_type)
                self.assertEqual(str(ee.exception), s)
        s = "width must be an integer"
        for invalid_type in self.invalid_types():
            with self.assertRaises(TypeError) as ee:
                setattr(rt, "width", invalid_type)
            self.assertEqual(str(ee.exception), s)

    def test_G_validate_value_negative_gt(self):
        '''Test property validation'''
        rt = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as ee:
                setattr(rt, attribute, -(randrange(10) + 1))
            self.assertEqual(str(ee.exception), s)

    def test_G_validate_value_negative_ge(self):
        '''Test property validation'''
        rt = Square(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as ee:
                setattr(rt, attribute, -(randrange(10) + 1))
            self.assertEqual(str(ee.exception), s)

    def test_G_validate_value_zero(self):
        '''Test property validation'''
        rt = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "width must be > 0".format(attribute)
            with self.assertRaises(ValueError) as ee:
                setattr(rt, attribute, 0)
            self.assertEqual(str(ee.exception), s)

    def test_H_property(self):
        '''Test property setting/getting'''
        rt = Square(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = randrange(10) + 1
            setattr(rt, attribute, n)
            self.assertEqual(getattr(rt, attribute), n)

    def test_H_property_range_zero(self):
        '''Test property setting/getting'''
        rt = Square(1, 2)
        rt.x = 0
        rt.y = 0
        self.assertEqual(rt.x, 0)
        self.assertEqual(rt.y, 0)

    # ----------------- Test #4 ------------------------
    def test_I_area_no_args(self):
        '''Test area() method signature'''
        rt = Square(5)
        with self.assertRaises(TypeError) as ee:
            Square.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(ee.exception), s)

    def test_I_area(self):
        '''Test area() method compution'''
        rt = Square(6)
        self.assertEqual(rt.area(), 36)
        w = randrange(10) + 1
        rt.size = w
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        rt = Square(w, 7, 8, 9)
        self.assertEqual(rt.area(), w * w)
        w = randrange(10) + 1
        rt = Square(w, y=7, x=8, id=9)
        self.assertEqual(rt.area(), w * w)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")
        self.assertEqual(s1.size, 10)

        with self.assertRaises(TypeError) as ee:
            s1.size = "9"
        self.assertEqual(str(ee.exception), "width must be an integer")

        with self.assertRaises(ValueError) as ee:
            s1.size = 0
        self.assertEqual(str(ee.exception), "width must be > 0")

    # ----------------- Test #5 & #7 ------------------------
    def test_J_display_no_args(self):
        '''Test display() method signature'''
        rt = Square(9)
        with self.assertRaises(TypeError) as ee:
            Square.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(ee.exception), s)

    def test_J_display_simple(self):
        '''Test display() method output'''
        rt = Square(1)
        f = io.StringIO()
        with redirect_stdout(f):
            rt.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)
        rt.size = 3
        f = io.StringIO()
        with redirect_stdout(f):
            rt.display()
        s = "\
###\n\
###\n\
###\n\
"
        self.assertEqual(f.getvalue(), s)
        rt = Square(5, 6, 7)
        f = io.StringIO()
        with redirect_stdout(f):
            rt.display()
        s = """\







      #####
      #####
      #####
      #####
      #####
"""
        self.assertEqual(f.getvalue(), s)
        rt = Square(9, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            rt.display()
        s = """\
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
        #########
"""
        self.assertEqual(f.getvalue(), s)
        rt = Square(1, 1, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            rt.display()
        s = """\










 #
"""
        self.assertEqual(f.getvalue(), s)

        rt = Square(5)
        f = io.StringIO()
        with redirect_stdout(f):
            rt.display()
        s = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        rt = Square(5, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            rt.display()
        s = """\
     #####
     #####
     #####
     #####
     #####
"""
        self.assertEqual(f.getvalue(), s)

        rt = Square(5, 3)
        f = io.StringIO()
        with redirect_stdout(f):
            rt.display()
        s = """\
   #####
   #####
   #####
   #####
   #####
"""
        self.assertEqual(f.getvalue(), s)

        rt = Square(5, 0, 4)
        f = io.StringIO()
        with redirect_stdout(f):
            rt.display()
        s = """\




#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        f = io.StringIO()
        with redirect_stdout(f):
            s1.display()
        s = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        self.assertEqual(s2.area(), 4)
        f = io.StringIO()
        with redirect_stdout(f):
            s2.display()
        s = """\
  ##
  ##
"""
        self.assertEqual(f.getvalue(), s)

        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")
        self.assertEqual(s3.area(), 9)
        f = io.StringIO()
        with redirect_stdout(f):
            s3.display()
        s = """\



 ###
 ###
 ###
"""
        self.assertEqual(f.getvalue(), s)

        # ----------------- Test #6 ------------------------

    def test_K_str_no_args(self):
        '''Test __str__() method signature'''
        rt = Square(5, 2)
        with self.assertRaises(TypeError) as ee:
            Square.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(ee.exception), s)

    def test_K_str(self):
        '''Test __str__() method return'''
        rt = Square(5)
        s = '[Square] (1) 0/0 - 5'
        self.assertEqual(str(rt), s)
        rt = Square(1, 1)
        s = '[Square] (2) 1/0 - 1'
        self.assertEqual(str(rt), s)
        rt = Square(3, 4, 5)
        s = '[Square] (3) 4/5 - 3'
        self.assertEqual(str(rt), s)
        rt = Square(10, 20, 30, 40)
        s = '[Square] (40) 20/30 - 10'
        self.assertEqual(str(rt), s)

        # ----------------- Test #8 & #9 ------------------------
    def test_L_update_no_args(self):
        '''Test update() method signature'''
        rt = Square(5, 2)
        with self.assertRaises(TypeError) as ee:
            Square.update()
        s = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(ee.exception), s)

        d = rt.__dict__.copy()
        rt.update()
        self.assertEqual(rt.__dict__, d)

    def test_L_update_args(self):
        '''Test update() postional args'''
        rt = Square(5, 2)
        d = rt.__dict__.copy()

        rt.update(10)
        d["id"] = 10
        self.assertEqual(rt.__dict__, d)

        rt.update(10, 5)
        d["_Rectangle__height"] = 5
        d["_Rectangle__width"] = 5
        self.assertEqual(rt.__dict__, d)

        rt.update(10, 5, 20)
        d["_Rectangle__x"] = 20
        self.assertEqual(rt.__dict__, d)

        rt.update(10, 5, 20, 25)
        d["_Rectangle__y"] = 25
        self.assertEqual(rt.__dict__, d)

    def test_L_update_args_bad(self):
        '''Test update() positional arg fubars'''
        rt = Square(5, 2)
        d = rt.__dict__.copy()

        rt.update(10)
        d["id"] = 10
        self.assertEqual(rt.__dict__, d)

        with self.assertRaises(ValueError) as ee:
            rt.update(10, -5)
        s = "width must be > 0"
        self.assertEqual(str(ee.exception), s)

        with self.assertRaises(ValueError) as ee:
            rt.update(10, 5, -17)
        s = "x must be >= 0"
        self.assertEqual(str(ee.exception), s)

        with self.assertRaises(ValueError) as ee:
            rt.update(10, 5, 17, -25)
        s = "y must be >= 0"
        self.assertEqual(str(ee.exception), s)

    def test_L_update_kwargs(self):
        '''Test update() keyword args'''
        rt = Square(5, 2)
        d = rt.__dict__.copy()

        rt.update(id=10)
        d["id"] = 10
        self.assertEqual(rt.__dict__, d)

        rt.update(size=17)
        d["_Rectangle__height"] = 17
        d["_Rectangle__width"] = 17
        self.assertEqual(rt.__dict__, d)

        rt.update(x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(rt.__dict__, d)

        rt.update(y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(rt.__dict__, d)

    def test_L_update_kwargs_2(self):
        '''Test update() keyword args'''
        rt = Square(5, 2)
        d = rt.__dict__.copy()

        rt.update(id=10)
        d["id"] = 10
        self.assertEqual(rt.__dict__, d)

        rt.update(id=10, size=5)
        d["_Rectangle__height"] = 5
        d["_Rectangle__width"] = 5
        self.assertEqual(rt.__dict__, d)

        rt.update(id=10, size=5, x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(rt.__dict__, d)

        rt.update(id=10, size=5, x=20, y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(rt.__dict__, d)

        rt.update(y=25, id=10, x=20, size=5)
        self.assertEqual(rt.__dict__, d)

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")

        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")

        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")

        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")

        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")

        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")

        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    # ----------------- Test #14 ------------------------
    def test_M_to_dictionary(self):
        '''Test to_dictionary() signature'''
        with self.assertRaises(TypeError) as ee:
            Square.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(ee.exception), s)

        rt = Square(1)
        d = {'x': 0, 'y': 0, 'size': 1, 'id': 1}
        self.assertEqual(rt.to_dictionary(), d)

        rt = Square(9, 2, 3, 4)
        d = {'x': 2, 'y': 3, 'size': 9, 'id': 4}
        self.assertEqual(rt.to_dictionary(), d)

        rt.x = 10
        rt.y = 20
        rt.size = 30
        d = {'x': 10, 'y': 20, 'size': 30, 'id': 4}
        self.assertEqual(rt.to_dictionary(), d)

        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        self.assertNotEqual(s1, s2)

if __name__ == "__main__":
    unittest.main()
