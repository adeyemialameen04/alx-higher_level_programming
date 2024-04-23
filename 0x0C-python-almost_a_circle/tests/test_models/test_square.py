#!/usr/bin/python3
"""Documenting module"""

import unittest
from models.base import Base
from models.square import Square

class TestSquare(unittest.TestCase):
    """Tests for the Square model"""

    def test_squ_init(self):
        squ_1 = Square(1, 2)
        self.assertEqual(squ_1.id, 6)
        squ_2 = Square(1, 2, 3)
        self.assertEqual(squ_2.id, squ_1.id + 1)
