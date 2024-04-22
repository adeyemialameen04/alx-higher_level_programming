#!/usr/bin/python3
"""Unittests for the Base class"""
import unittest
import json
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):
    """Class for testing base class"""

    def test_normal(self):
        """Tests normally"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 3, b2.id + 2)

    def test_id(self):
        """Tests if id is working"""
        b1 = Base(20)
        b2 = Base(40)
        self.assertEqual(20, b1.id)
        self.assertEqual(b2.id, b1.id * 2)

    def test_to_json(self):
        """Tests if to_json is working """
        rec1 = Rectangle(8, 120, 131, 9078, 112)
        rec2 = Rectangle(9, 18, 36, 72, 14)
        dict_1 = rec1.to_dictionary()
        dict_2 = rec2.to_dictionary()
        json_string = Base.to_json_string([dict_1, dict_2])
        parsed_json = json.loads(json_string)
        self.assertEqual(parsed_json[0]['id'], 112)
        self.assertEqual(parsed_json[1]['x'], 36)

    def test_from_json(self):
        """"""
        squ = Square(12, 24, 48, 10)
        squ_dict = squ.to_dictionary()
        squ_json = Base.to_json_string([squ_dict])
        squ_obj = Base.from_json_string(squ_json)
        self.assertEqual(squ_obj[0]["x"], 24)
        self.assertTrue(type(squ_obj[0]), dict)

    # def test_save_to_file(self):
    #     """Tests for save to file"""
    #     # For squs
    #     squ = Square(9, 18, 16, 113)
    #     squ_2 = Square(42, 29, 20, 20)
    #     Base.save_to_file([squ, squ_2])
    #     with open('Square.json', 'r', encoding='utf-8') as file:
    #         read = file.read()
    #     dicts_lists = json.loads(read)
    #     self.assertEqual(dicts_lists[0]['id'], 113)
    #     self.assertEqual(dicts_lists[1]['x'], 29)
    #
    #     # For recs
    #     rec_1 = Rectangle(5, 6, 3, 3, 30)
    #     rec_2 = Rectangle(7, 8, 4, 4, 40)
    #     Base.save_to_file([rec_1, rec_2])
    #     with open('Rectangle.json', 'r', encoding='utf-8') as file:
    #         read = file.read()
    #     dicts_lists = json.loads(read)
    #     self.assertEqual(dicts_lists[0]['id'], 30)
    #     self.assertEqual(dicts_lists[1]['x'], 4)

    # def test_more_save_to_file(self):
