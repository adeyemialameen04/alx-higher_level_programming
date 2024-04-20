#!/usr/bin/python3
"""Unittests for the Base class"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Class for testing base class"""

    def test_normal(self):
        """Tests normally"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 3, b2.id + 2)

    def test_id(self):
        b1 = Base(20)
        b2 = Base(40)
        self.assertEqual(20, b1.id)
        self.assertEqual(b2.id, b1.id * 2)
