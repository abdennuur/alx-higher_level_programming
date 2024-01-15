#!/usr/bin/python3
'''Module for THE rectangle unit tests'''
import unittest
from models.base import Base
from models.rectangle import Rectangle
from random import randrange
from contextlib import redirect_stdout
import io


class TestRectangle(unittest.TestCase):
    '''Test Base class'''

    def setUp(self):
        '''Import module, instantiate class'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Clean up after each test_method'''
        pass

    # ----------------- Test #2 ------------------------

    def test_A_class(self):
        '''Test Rectangle class type'''
        self.assertEqual(str(Rectangle),
                         "<class 'models.rectangle.Rectangle'>")

    def test_B_inheritance(self):
        '''Test -> Rectangle inherit Base'''
        self.assertTrue(issubclass(Rectangle, Base))

    def test_C_constructor_no_args(self):
        '''Test the constructor signature'''
        with self.assertRaises(TypeError) as ee:
            rt = Rectangle()
        st = "__init__() missing 2 required positional arguments: 'width' \
and 'height'"
        self.assertEqual(str(ee.exception), st)

    def test_C_constructor_many_args(self):
        '''Test constructor signature'''
        with self.assertRaises(TypeError) as ee:
            rt = Rectangle(1, 2, 3, 4, 5, 6)
        st = "__init__() takes from 3 to 6 positional arguments but 7 were \
given"
        self.assertEqual(str(ee.exception), st)

    def test_C_constructor_one_args(self):
        '''Test constructor signature'''
        with self.assertRaises(TypeError) as ee:
            rt = Rectangle(1)
        st = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(ee.exception), st)

    def test_D_instantiation(self):
        '''Test instantiation'''
        rt = Rectangle(10, 20)
        self.assertEqual(str(type(rt)), "<class 'models.rectangle.Rectangle'>")
        self.assertTrue(isinstance(rt, Base))
        d = {'_Rectangle__height': 20, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(rt.__dict__, d)

        with self.assertRaises(TypeError) as ee:
            rt = Rectangle("1", 2)
        mesg = "width must be an integer"
        self.assertEqual(str(ee.exception), mesg)

        with self.assertRaises(TypeError) as ee:
            rt = Rectangle(1, "2")
        mesg = "height must be an integer"
        self.assertEqual(str(ee.exception), mesg)

        with self.assertRaises(TypeError) as ee:
            rt = Rectangle(1, 2, "3")
        mesg = "x must be an integer"
        self.assertEqual(str(ee.exception), mesg)

        with self.assertRaises(TypeError) as ee:
            rt = Rectangle(1, 2, 3, "4")
        mesg = "y must be an integer"
        self.assertEqual(str(ee.exception), mesg)

        with self.assertRaises(ValueError) as ee:
            rt = Rectangle(-1, 2)
        mesg = "width must be > 0"
        self.assertEqual(str(ee.exception), mesg)

        with self.assertRaises(ValueError) as ee:
            rt = Rectangle(1, -2)
        mesg = "height must be > 0"
        self.assertEqual(str(ee.exception), mesg)

        with self.assertRaises(ValueError) as ee:
            rt = Rectangle(0, 2)
        mesg = "width must be > 0"
        self.assertEqual(str(ee.exception), mesg)

        with self.assertRaises(ValueError) as ee:
            rt = Rectangle(1, 0)
        mesg = "height must be > 0"
        self.assertEqual(str(ee.exception), mesg)

        with self.assertRaises(ValueError) as ee:
            rt = Rectangle(1, 2, -3)
        mesg = "x must be >= 0"
        self.assertEqual(str(ee.exception), mesg)

        with self.assertRaises(ValueError) as ee:
            rt = Rectangle(1, 2, 3, -4)
        mesg = "y must be >= 0"
        self.assertEqual(str(ee.exception), mesg)

    def test_D_instantiation_positional(self):
        '''Test positional instantiation'''
        rt = Rectangle(5, 10, 15, 20)
        d = {'_Rectangle__height': 10, '_Rectangle__width': 5,
             '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 1}
        self.assertEqual(rt.__dict__, d)

        rt = Rectangle(5, 10, 15, 20, 98)
        d = {'_Rectangle__height': 10, '_Rectangle__width': 5,
             '_Rectangle__x': 15, '_Rectangle__y': 20, 'id': 98}
        self.assertEqual(rt.__dict__, d)

    def test_D_instantiation_keyword(self):
        '''Tests positional instantiation.'''
        rt = Rectangle(100, 200, id=421, y=99, x=101)
        d = {'_Rectangle__height': 200, '_Rectangle__width': 100,
             '_Rectangle__x': 101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(rt.__dict__, d)

    def test_E_id_inherited(self):
        '''Test if id is inherited frm Base'''
        Base._Base__nb_objects = 98
        rt = Rectangle(2, 4)
        self.assertEqual(rt.id, 99)

    def test_F_properties(self):
        '''Test property getters/setters'''
        rt = Rectangle(5, 9)
        rt.width = 100
        rt.height = 101
        rt.x = 102
        rt.y = 103
        d = {'_Rectangle__height': 101, '_Rectangle__width': 100,
             '_Rectangle__x': 102, '_Rectangle__y': 103, 'id': 1}
        self.assertEqual(rt.__dict__, d)
        self.assertEqual(rt.width, 100)
        self.assertEqual(rt.height, 101)
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
        rt = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            s = "{} must be an integer".format(attribute)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as ee:
                    setattr(rt, attribute, invalid_type)
                self.assertEqual(str(ee.exception), s)

    def test_G_validate_value_negative_gt(self):
        '''Test property validatio'''
        rt = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            s = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as ee:
                setattr(rt, attribute, -(randrange(10) + 1))
            self.assertEqual(str(ee.exception), s)

    def test_G_validate_value_negative_ge(self):
        '''Test property validation'''
        rt = Rectangle(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be >= 0".format(attribute)
            with self.assertRaises(ValueError) as ee:
                setattr(rt, attribute, -(randrange(10) + 1))
            self.assertEqual(str(ee.exception), s)

    def test_G_validate_value_zero(self):
        '''Test property validation'''
        rt = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            s = "{} must be > 0".format(attribute)
            with self.assertRaises(ValueError) as ee:
                setattr(rt, attribute, 0)
            self.assertEqual(str(ee.exception), s)

    def test_H_property(self):
        '''Test property setting/getting'''
        rt = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = randrange(10) + 1
            setattr(rt, attribute, n)
            self.assertEqual(getattr(rt, attribute), n)

    def test_H_property_range_zero(self):
        '''Test property setting/getting'''
        rt = Rectangle(1, 2)
        rt.x = 0
        rt.y = 0
        self.assertEqual(rt.x, 0)
        self.assertEqual(rt.y, 0)

    # ----------------- Test #4 ------------------------
    def test_I_area_no_args(self):
        '''Test area() method signature'''
        rt = Rectangle(5, 6)
        with self.assertRaises(TypeError) as ee:
            Rectangle.area()
        s = "area() missing 1 required positional argument: 'self'"
        self.assertEqual(str(ee.exception), s)

    def test_I_area(self):
        '''Test area() method compuation'''
        rt = Rectangle(5, 6)
        self.assertEqual(rt.area(), 30)
        w = randrange(10) + 1
        h = randrange(10) + 1
        rt.width = w
        rt.height = h
        self.assertEqual(rt.area(), w * h)
        w = randrange(10) + 1
        h = randrange(10) + 1
        rt = Rectangle(w, h, 7, 8, 9)
        self.assertEqual(rt.area(), w * h)
        w = randrange(10) + 1
        h = randrange(10) + 1
        rt = Rectangle(w, h, y=7, x=8, id=9)
        self.assertEqual(rt.area(), w * h)

        rt1 = Rectangle(3, 2)
        self.assertEqual(rt1.area(), 6)

        rt2 = Rectangle(2, 10)
        self.assertEqual(rt2.area(), 20)

        rt3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rt3.area(), 56)

    # ----------------- Test #5 & #7 ------------------------
    def test_J_display_no_args(self):
        '''Test display() method signature'''
        rt = Rectangle(9, 8)
        with self.assertRaises(TypeError) as ee:
            Rectangle.display()
        s = "display() missing 1 required positional argument: 'self'"
        self.assertEqual(str(ee.exception), s)

    def test_J_display_simple(self):
        '''Test display() method output'''
        rt = Rectangle(1, 1)
        f = io.StringIO()
        with redirect_stdout(f):
            rt.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)
        rt.width = 3
        rt.height = 5
        f = io.StringIO()
        with redirect_stdout(f):
            rt.display()
        s = "\
###\n\
###\n\
###\n\
###\n\
###\n\
"
        self.assertEqual(f.getvalue(), s)
        rt = Rectangle(5, 6, 7, 8)
        f = io.StringIO()
        with redirect_stdout(f):
            rt.display()
        s = """







       #####
       #####
       #####
       #####
       #####
       #####
"""
        self.assertEqual(f.getvalue(), s)
        rt = Rectangle(9, 8)
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
"""
        self.assertEqual(f.getvalue(), s)
        rt = Rectangle(1, 1, 10, 10)
        f = io.StringIO()
        with redirect_stdout(f):
            rt.display()
        s = """\










          #
"""
        self.assertEqual(f.getvalue(), s)

        rt = Rectangle(5, 5)
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

        rt = Rectangle(5, 3, 5)
        f = io.StringIO()
        with redirect_stdout(f):
            rt.display()
        s = """\
     #####
     #####
     #####
"""
        self.assertEqual(f.getvalue(), s)

        rt = Rectangle(5, 3, 0, 4)
        f = io.StringIO()
        with redirect_stdout(f):
            rt.display()
        s = """\




#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        # ----------------- Test #6 ------------------------

    def test_K_str_no_args(self):
        '''Test __str__() method signature'''
        rt = Rectangle(5, 2)
        with self.assertRaises(TypeError) as ee:
            Rectangle.__str__()
        s = "__str__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(ee.exception), s)

    def test_K_str(self):
        '''Tests __str__() method return.'''
        rt = Rectangle(5, 2)
        s = '[Rectangle] (1) 0/0 - 5/2'
        self.assertEqual(str(rt), s)
        rt = Rectangle(1, 1, 1)
        s = '[Rectangle] (2) 1/0 - 1/1'
        self.assertEqual(str(rt), s)
        rt = Rectangle(3, 4, 5, 6)
        s = '[Rectangle] (3) 5/6 - 3/4'
        self.assertEqual(str(rt), s)

        Base._Base__nb_objects = 0
        rt1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(rt1), "[Rectangle] (12) 2/1 - 4/6")

        rt2 = Rectangle(5, 5, 1)
        self.assertEqual(str(rt2), "[Rectangle] (1) 1/0 - 5/5")

        # ----------------- Test #8 & #9 ------------------------
    def test_L_update_no_args(self):
        '''Test update() method signature'''
        rt = Rectangle(5, 2)
        with self.assertRaises(TypeError) as ee:
            Rectangle.update()
        s = "update() missing 1 required positional argument: 'self'"
        self.assertEqual(str(ee.exception), s)

        d = rt.__dict__.copy()
        rt.update()
        self.assertEqual(rt.__dict__, d)

    def test_L_update_args(self):
        '''Test update() postional args'''
        rt = Rectangle(5, 2)
        d = rt.__dict__.copy()

        rt.update(10)
        d["id"] = 10
        self.assertEqual(rt.__dict__, d)

        rt.update(10, 5)
        d["_Rectangle__width"] = 5
        self.assertEqual(rt.__dict__, d)

        rt.update(10, 5, 17)
        d["_Rectangle__height"] = 17
        self.assertEqual(rt.__dict__, d)

        rt.update(10, 5, 17, 20)
        d["_Rectangle__x"] = 20
        self.assertEqual(rt.__dict__, d)

        rt.update(10, 5, 17, 20, 25)
        d["_Rectangle__y"] = 25
        self.assertEqual(rt.__dict__, d)

    def test_L_update_args_bad(self):
        '''Test update() positional arg fubar'''
        rt = Rectangle(5, 2)
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
        s = "height must be > 0"
        self.assertEqual(str(ee.exception), s)

        with self.assertRaises(ValueError) as ee:
            rt.update(10, 5, 17, -20)
        s = "x must be >= 0"
        self.assertEqual(str(ee.exception), s)

        with self.assertRaises(ValueError) as ee:
            rt.update(10, 5, 17, 20, -25)
        s = "y must be >= 0"
        self.assertEqual(str(ee.exception), s)

    def test_L_update_kwargs(self):
        '''Test update() keyword args'''
        rt = Rectangle(5, 2)
        d = rt.__dict__.copy()

        rt.update(id=10)
        d["id"] = 10
        self.assertEqual(rt.__dict__, d)

        rt.update(width=5)
        d["_Rectangle__width"] = 5
        self.assertEqual(rt.__dict__, d)

        rt.update(height=17)
        d["_Rectangle__height"] = 17
        self.assertEqual(rt.__dict__, d)

        rt.update(x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(rt.__dict__, d)

        rt.update(y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(rt.__dict__, d)

    def test_L_update_kwargs_2(self):
        '''Test update() keyword args'''
        rt = Rectangle(5, 2)
        d = rt.__dict__.copy()

        rt.update(id=10)
        d["id"] = 10
        self.assertEqual(rt.__dict__, d)

        rt.update(id=10, width=5)
        d["_Rectangle__width"] = 5
        self.assertEqual(rt.__dict__, d)

        rt.update(id=10, width=5, height=17)
        d["_Rectangle__height"] = 17
        self.assertEqual(rt.__dict__, d)

        rt.update(id=10, width=5, height=17, x=20)
        d["_Rectangle__x"] = 20
        self.assertEqual(rt.__dict__, d)

        rt.update(id=10, width=5, height=17, x=20, y=25)
        d["_Rectangle__y"] = 25
        self.assertEqual(rt.__dict__, d)

        rt.update(y=25, id=10, height=17, x=20, width=5)
        self.assertEqual(rt.__dict__, d)

        Base._Base__nb_objects = 0
        rt1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rt1), "[Rectangle] (1) 10/10 - 10/10")

        rt1.update(height=1)
        self.assertEqual(str(rt1), "[Rectangle] (1) 10/10 - 10/1")

        rt1.update(width=1, x=2)
        self.assertEqual(str(rt1), "[Rectangle] (1) 2/10 - 1/1")

        rt1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(rt1), "[Rectangle] (89) 3/1 - 2/1")

        rt1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(rt1), "[Rectangle] (89) 1/3 - 4/2")

        Base._Base__nb_objects = 0
        rt1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(rt1), "[Rectangle] (1) 10/10 - 10/10")

        rt1.update(89)
        self.assertEqual(str(rt1), "[Rectangle] (89) 10/10 - 10/10")

        rt1.update(89, 2)
        self.assertEqual(str(rt1), "[Rectangle] (89) 10/10 - 2/10")

        rt1.update(89, 2, 3)
        self.assertEqual(str(rt1), "[Rectangle] (89) 10/10 - 2/3")

        rt1.update(89, 2, 3, 4)
        self.assertEqual(str(rt1), "[Rectangle] (89) 4/10 - 2/3")

        rt1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rt1), "[Rectangle] (89) 4/5 - 2/3")

    # ----------------- Test #13 ------------------------
    def test_M_to_dictionary(self):
        '''Test to_dictionary() signature'''
        with self.assertRaises(TypeError) as ee:
            Rectangle.to_dictionary()
        s = "to_dictionary() missing 1 required positional argument: 'self'"
        self.assertEqual(str(ee.exception), s)

        rt = Rectangle(1, 2)
        d = {'x': 0, 'y': 0, 'width': 1, 'id': 1, 'height': 2}
        self.assertEqual(rt.to_dictionary(), d)

        rt = Rectangle(1, 2, 3, 4, 5)
        d = {'x': 3, 'y': 4, 'width': 1, 'id': 5, 'height': 2}
        self.assertEqual(rt.to_dictionary(), d)

        rt.x = 10
        rt.y = 20
        rt.width = 30
        rt.height = 40
        d = {'x': 10, 'y': 20, 'width': 30, 'id': 5, 'height': 40}
        self.assertEqual(rt.to_dictionary(), d)

        rt1 = Rectangle(10, 2, 1, 9)
        rt1_dictionary = rt1.to_dictionary()
        rt2 = Rectangle(1, 1)
        rt2.update(**rt1_dictionary)
        self.assertEqual(str(rt1), str(rt2))
        self.assertNotEqual(rt1, rt2)

if __name__ == "__main__":
    unittest.main()
