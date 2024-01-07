#!/usr/bin/python3
"""unit test for the max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unit test class for themax_integer"""
    def test_module_docstring(self):
        """tests for the module docsting"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Tests for the funstion docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_list(self):
        """Tests for the empty list []"""
        e = []
        self.assertIsNone(max_integer(e))

    def test_no_args(self):
        """Tests for no arguments passed to the func"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Tests for the only one number in the list"""
        o = [1]
        self.assertEqual(max_integer(o), 1)

    def test_positive_end(self):
        """Tests for all positive with max at the end"""
        e = [2, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(e), 50)

    def test_positive_middle(self):
        """Tests for all positive with max in the middle"""
        m = [2, 10, 8, 360, 14, 50]
        self.assertEqual(max_integer(m), 360)

    def test_positive_beginning(self):
        """Tests for all positive with max at the beginning"""
        b = [200, 10, 8, 36, 14, 50]
        self.assertEqual(max_integer(b), 200)

    def test_one_negative(self):
        """Test for the  list with one negative number"""
        on = [200, 10, 8, -36, 14, 50]
        self.assertEqual(max_integer(on), 200)

    def test_all_negative(self):
        """Test for list with all negative nmbers"""
        n = [-6, -50, -75, -1, -100]
        self.assertEqual(max_integer(n), -1)

    def test_none(self):
        """Tests for passing none as arg"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Tests for non-int type in list"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)

if __name__ == "__main__":
    unittest.main()
