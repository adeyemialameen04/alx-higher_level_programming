#!/usr/bin/python3
"""Unittests for the Base class"""
import unittest
import os
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

    def test_save_to_file(self):
        squ = Square(3, 1, 1, 10)
        squ_2 = Square(4, 2, 2, 20)
        rec_1 = Rectangle(5, 6, 3, 3, 30)
        r2 = Rectangle(7, 8, 4, 4, 40)
        Base.save_to_file([squ, squ_2])
        with open('Square.json', 'r', encoding='utf-8') as file:
            text = file.read()
        list_of_dicts = eval(text)
        self.assertEqual(list_of_dicts[0]['id'], 10)
        self.assertEqual(list_of_dicts[1]['x'], 2)

        Base.save_to_file([rec_1, r2])
        with open('Rectangle.json', 'r', encoding='utf-8') as file:
            text = file.read()
        list_of_dicts = eval(text)
        self.assertEqual(list_of_dicts[0]['id'], 30)
        self.assertEqual(list_of_dicts[1]['x'], 4)

    def test_more_save_to_file(self):
        squ = Square(3, 1, 1, 10)
        squ_2 = Square(4, 2, 2, 20)
        rec_1 = Rectangle(5, 6, 3, 3, 30)
        r2 = Rectangle(7, 8, 4, 4, 40)
        Base.save_to_file(["str", 42, "yare yare", True, squ, squ_2])
        with open('Square.json', 'r', encoding='utf-8') as file:
            text = file.read()
        list_of_dicts = eval(text)
        self.assertEqual(list_of_dicts[0]['id'], 10)
        self.assertEqual(list_of_dicts[1]['x'], 2)

        Base.save_to_file([squ, 89, rec_1, "gambare", 42, squ_2, r2])
        with open('Rectangle.json', 'r', encoding='utf-8') as file:
            text = file.read()
        list_of_dicts = eval(text)
        self.assertEqual(list_of_dicts[1]['id'], 30)
        self.assertEqual(list_of_dicts[3]['x'], 4)

    def test_save_t_file_empty(self):
        Base.save_to_file([])
        with open('Rectangle.json', 'r', encoding='utf-8') as file:
            text = file.read()
        self.assertEqual(text, "[]")

    def test_from_json_empty_file(self):
        d_list = Base.from_json_string("")
        self.assertEqual(len(d_list), 0)
        d_list = Base.from_json_string(None)
        self.assertEqual(len(d_list), 0)

    def test_create(self):
        r = Rectangle(9, 2, 3, 4, 45)
        squ = Square(4, 8, 9, 2)
        r_d = r.to_dictionary()
        s_d = squ.to_dictionary()
        r2 = Rectangle.create(**r_d)
        squ_2 = Square.create(**s_d)
        self.assertEqual(squ.id, squ_2.id)
        self.assertEqual(r.id, r2.id)
        self.assertEqual(squ.y, squ_2.y)
        self.assertEqual(squ.x, squ_2.x)
        self.assertEqual(r.width, r2.width)
        self.assertEqual(squ.size, squ_2.size)

    def test_read_from_file(self):
        rec_1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [rec_1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output[0].y, 8)
        self.assertEqual(list_rectangles_output[1].height, 4)

    def test_read_from_file_basic(self):
        rec_1 = Rectangle(10, 7, 8, 3, 44)
        r2 = Rectangle(24, 23, 5, 1, 99)
        Rectangle.save_to_file([rec_1, r2])
        with open('Rectangle.json', 'r', encoding='utf-8') as file:
            text = file.read()
        rects = Rectangle.load_from_file()
        self.assertEqual(rects[0].width, 10)
        self.assertEqual(rects[1].id, 99)
        self.assertEqual(rects[1].x, 5)

    def test_read_from_file_empty(self):
        """tests the base class method to read from json files when
            -> empty
        """
        try:
            os.remove('Square.json')
        except:
            pass
        list_output = Square.load_from_file()
        self.assertEqual(len(list_output), 0)
        self.assertEqual(list, type(list_output))

    def test_write_csv_basic(self):
        """tests the base class method to write instances as csv
        """
        rec_1 = Rectangle(10, 7, 2, 8, 33)
        r2 = Rectangle(10, 8, 4, 9, 44)
        Rectangle.save_to_file_csv([rec_1, r2])
        with open('Rectangle.csv', 'r', encoding='utf-8') as file:
            text = file.readlines()
        self.assertEqual(text[0][0] + text[0][1], "33")
        self.assertEqual(text[1][0] + text[1][1], "44")

    def test_write_csv_complex(self):
        """tests the base class method to write instances as csv
            -> with bad input etc
        """
        rec_1 = Rectangle(10, 7, 2, 4, 33)
        r2 = Rectangle(10, 8, 4, 9, 44)
        s1 = Square(10, 8, 4, 109)
        squ_2 = Square(11, 4, 3, 120)
        bs = ["bs", 42, True]
        more_bs = 45.34
        Rectangle.save_to_file_csv([bs, s1, squ_2, more_bs, r2, rec_1])
        with open('Rectangle.csv', 'r', encoding='utf-8') as file:
            text = file.readlines()
        self.assertEqual(text[0][0] + text[0][1] + text[0][2], "109")
        self.assertEqual(text[3][0] + text[3][1], "33")

    def test_read_csv_basic(self):
        """tests the base class method to read from csv
            -> basic input
        """
        rec_1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [rec_1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_output = Rectangle.load_from_file_csv()
        self.assertEqual(8, list_output[0].y)
        self.assertEqual(4, list_output[1].height)

    def test_read_csv_complex(self):
        """tests the base class method to read from csv
            -> complex input, can contain squares in rectangle file
            -> squares should be returned as rectangles
        """
        rec_1 = Rectangle(10, 7, 2, 8)
        s1 = Square(2, 4)
        list_rectangles_input = [rec_1, s1]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_output = Rectangle.load_from_file_csv()
        self.assertEqual(8, list_output[0].y)
        self.assertEqual(4, list_output[1].height)

    def test_read_csv_empty(self):
        try:
            os.remove('Square.csv')
        except:
            pass
        list_output = Square.load_from_file_csv()
        self.assertEqual(0, len(list_output))
        self.assertEqual(list, type(list_output))