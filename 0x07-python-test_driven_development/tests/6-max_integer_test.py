#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_normal(self):
        """Testing for normal all +ve"""
        self.assertEqual(max_integer([1, 2, 9]), 9)
        self.assertEqual(max_integer([1, -2, 7.9, 8]), 8)

    def test_none(self):
        """Testing for None"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Testing for a non-int in list"""
        test_arr = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(test_arr)

    def test_max_at_beginning(self):
        """Testing at beginning"""
        test_arr = [30, 10, 1]
        self.assertEqual((max_integer(test_arr), 30))

    def test_all_negative(self):
        """Testing for all negative"""
        # test_arr = [-3, -90, -2, -8]
        self.assertEqual(max_integer([-3, -90, -2, -8]), -2)

    def test_empty_arr(self):
        """Testing for empty array"""
        self.assertIsNone(max_integer([]))

    def test_0(self):
        """Testing for 0 and multiple 0's in array"""
        self.assertEqual(max_integer([0, 0, 0, 0, ]), 0)
        self.assertEqual(max_integer([0]), 0)

    def test_0_negative(self):
        "Testing for -ve and multiple -ve 0's in array"
        self.assertEqual(max_integer([-0]), 0)
        self.assertEqual(max_integer([-0, -0]), 0)

    def test_no_args(self):
        """Testing for no args in array"""
        self.assertIsNone(max_integer())

    def test_list_of_list(self):
        """Testing for lists of lists in array."""
        with self.assertRaises(TypeError):
            max_integer([10, 20, [-1, 2]])

    def test_1_element(self):
        self.assertEqual(max_integer([3]), 3)

    def test_2_args(self):
        """Testing for 2args"""
        with self.assertRaises(TypeError):
            max_integer([10, 20], 20)
