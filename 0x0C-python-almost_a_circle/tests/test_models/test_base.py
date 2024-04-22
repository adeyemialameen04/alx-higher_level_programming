#!/usr/bin/python3
"""This module define a test suite"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
from io import StringIO
import os


class TestBase(unittest.TestCase):
    """This class defines series test suite"""

    def setUp(self):
        """This method creates Base class instances"""

        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()
        self.b6 = Base()

    def tearDown(self):
        """This method resets class attribute to 0 so that
        new instances can have non-incremental values for
        their id attributes"""

        Base._Base__nb_objects = 0

    def test_class_type(self):
        """The method checks whether object instance
        was created correctly"""

        self.assertEqual(self.b1.__class__.__name__, "Base")
        self.assertEqual(type(self.b1), Base)
        self.assertTrue(isinstance(self.b1, Base))

    def test_attribute(self):
        """Test to ensure attribute is correctly instantiated"""

        self.assertTrue(hasattr(self.b1, 'id'))

    def test_unique_id(self):
        """The method tests if unique id' are created for each instance"""

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)

    def test_custom_id(self):
        """This method tests if instances have a custom id when id is not
        None"""

        self.assertEqual(self.b4.id, 12)

    def test_incremental_id(self):
        """This method tests if the id attribute is incremented correctly"""

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertNotEqual(self.b4.id, 4)
        self.assertEqual(self.b5.id, 4)
        self.assertEqual(self.b6.id, 5)

    def test_to_json_string(self):
        """Test for json string representation"""

        self.r1 = Rectangle(10, 7, 2, 8)
        self.s1 = Square(5)
        dictionary = self.r1.to_dictionary()
        dictionary_ = self.s1.to_dictionary()

        with self.assertRaises(TypeError):
            self.json_dictionary = Base.to_json_string()
        with self.assertRaises(TypeError):
            self.json_dictionary = Base.to_json_string(2)

        self.json_dictionary = Base.to_json_string(None)
        self.assertEqual(self.json_dictionary, "[]")

        self.json_dictionary = Base.to_json_string([])
        self.assertEqual(self.json_dictionary, "[]")

        self.json_dictionary = Base.to_json_string([{}])
        self.assertEqual(self.json_dictionary, "[{}]")

        self.json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(type(self.json_dictionary) == str)

        self.json_dictionary = Square.to_json_string([dictionary, dictionary_])
        self.assertTrue(type(self.json_dictionary) == str)

    def test_save_to_file(self):
        """Test for JSON string to a file"""

        self.tearDown()

        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)
        self.s1 = Square(5)
        self.s2 = Square(1, 2, 5)

        filename_1 = "{:s}.json".format(self.r1.__class__.__name__)
        filename_2 = "{:s}.json".format(self.s1.__class__.__name__)

        Rectangle.save_to_file([self.r1, self.r2])
        Square.save_to_file([self.s1, self.s2])

        with open(filename_1, "r") as file:
            f = file.read()
            self.assertTrue(type(f) == str)

        with open(filename_2, "r") as file:
            self.assertTrue(type(file.read()) == str)

        Square.save_to_file([self.r1])
        with open(filename_2, "r") as file:
            self.assertTrue(type(file.read()) == str)

        Square.save_to_file([])
        with open(filename_2, "r") as file:
            self.assertEqual(file.read(), "[]")

        Rectangle.save_to_file(None)
        with open(filename_1, "r") as file:
            self.assertEqual(file.read(), "[]")

        Rectangle.save_to_file([self.r1, self.s2])
        with open(filename_1, "r") as file:
            self.assertTrue(type(file.read()) == str)

        Rectangle.save_to_file({self.s1, self.s2})
        with open(filename_1, "r") as file:
            self.assertTrue(type(file.read()) == str)

        Square.save_to_file("")
        with open(filename_2, "r") as file:
            self.assertEqual(file.read(), "[]")

        Square.save_to_file([self.r1, self.s2])
        with open(filename_2, "r") as file:
            self.assertTrue(type(file.read()) == str)
        with open(filename_2, "r") as file:
            self.assertTrue("size" in file.read())

        Rectangle.save_to_file({})
        with open(filename_1, "r") as file:
            self.assertEqual(file.read(), "[]")

        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
        with self.assertRaises(TypeError):
            Square.save_to_file()
        with self.assertRaises(AttributeError):
            Square.save_to_file([34])
        with self.assertRaises(TypeError):
            Square.save_to_file(34)
        with self.assertRaises(AttributeError):
            Square.save_to_file([""])
        with self.assertRaises(AttributeError):
            Square.save_to_file([None])

    def test_from_json_string(self):
        """Tests for converting json string to dictionary"""

        self.tearDown()

        self.r1 = Rectangle(10, 7, 2, 8)
        self.s1 = Square(1, 2, 5)

        r1_dict = self.r1.to_dictionary()
        s1_dict = self.s1.to_dictionary()

        json_string = Base.to_json_string([r1_dict, s1_dict])

        json_to_obj = Base.from_json_string(json_string)
        self.assertTrue(type(json_to_obj), list)
        self.assertTrue(type(json_to_obj[0]), dict)

        json_to_obj = Base.from_json_string([])
        self.assertEqual(json_to_obj, [])

        json_to_obj = Base.from_json_string(None)
        self.assertEqual(json_to_obj, [])

    def test_create(self):
        """Test creating of instance from dictionary"""

        self.tearDown()

        self.r2 = Rectangle(3, 5, 1)
        r2_dictionary = self.r2.to_dictionary()
        self.r3 = Rectangle.create(**r2_dictionary)

        self.assertTrue(type(self.r3) == Rectangle)
        self.assertFalse(self.r2 is self.r3)
        self.assertFalse(self.r3 == self.r2)
        self.assertTrue(isinstance(self.r2, Rectangle))
        self.assertTrue(isinstance(self.r3, Rectangle))

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r2)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (1) 1/0 - 3/5"
        self.assertEqual(printed_output, expected_output)

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r3)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (1) 1/0 - 3/5"
        self.assertEqual(printed_output, expected_output)

        # reset stdout to terminal output
        sys.stdout = sys.__stdout__

    def test_load_from_file(self):
        """Test for instances reconstructed from file"""

        self.tearDown()

        # Test for Rectangle Class
        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)

        list_rectangles_input = [self.r1, self.r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()

        self.assertTrue(type(list_rectangles_output) == list)

        for rect in list_rectangles_input:
            self.assertEqual(type(rect), Rectangle)
            self.assertTrue(isinstance(rect, Rectangle))

        for rect in list_rectangles_output:
            self.assertEqual(type(rect), Rectangle)
            self.assertTrue(isinstance(rect, Rectangle))

        self.assertFalse(list_rectangles_input is list_rectangles_output)
        self.assertFalse(list_rectangles_input[0] is list_rectangles_output[0])

        # Test for Square Class
        self.s1 = Square(5)
        self.s2 = Square(7, 9, 1)

        list_squares_input = [self.s1, self.s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()

        self.assertTrue(type(list_squares_output) == list)

        for square in list_squares_input:
            self.assertEqual(type(square), Square)
            self.assertTrue(isinstance(square, Square))

        self.assertFalse(list_squares_input is list_squares_output)
        self.assertFalse(list_squares_input[0] is list_squares_output[0])

    def save_to_file_csv(self):
        """Test for serialization into CSV file"""

        self.tearDown()

        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)
        self.s1 = Square(5)
        self.s2 = Square(1, 2, 5)

        filename_1 = "{:s}.csv".format(self.r1.__class__.__name__)
        filename_2 = "{:s}.csv".format(self.s1.__class__.__name__)

        Rectangle.save_to_file_csv([self.r1, self.r2])
        Square.save_to_file_csv([self.s1, self.s2])

        with open(filename_1, "r", encoding='utf-8') as csv_file:
            output_reader = csv.reader(csv_file)
            for row in output_reader:
                self.assertTrue(type(row) == list)

        with open(filename_2, "r", encoding='utf-8') as csv_file:
            output_reader = csv.reader(csv_file)
            for row in output_reader:
                self.assertTrue(type(row) == list)

        Square.save_to_file_csv([self.s1, self.s2])
        self.assertTrue(os.path.exists("Square.csv"))

        Rectangle.save_to_file_csv([self.r1, self.r2])
        self.assertTrue(os.path.exists("Rectangle.csv"))

        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()
        with self.assertRaises(TypeError):
            Square.save_to_file_csv()
        with self.assertRaises(AttributeError):
            Square.save_to_file_csv([34])
        with self.assertRaises(TypeError):
            Square.save_to_file_csv(34)
        with self.assertRaises(AttributeError):
            Square.save_to_file_csv([""])
        with self.assertRaises(AttributeError):
            Square.save_to_file_csv([None])

    def load_from_file_csv(self):
        """Test for de-serialization from a CSV file"""

        self.tearDown()

        # Test for Rectangle Class
        self.r1 = Rectangle(10, 7, 2, 8)
        self.r2 = Rectangle(2, 4)

        list_rectangles_input = [self.r1, self.r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()

        self.assertTrue(type(list_rectangles_output) == list)

        for rect in list_rectangles_output:
            self.assertEqual(type(rect), Rectangle)
            self.assertTrue(isinstance(rect, Rectangle))

        for rect in list_rectangles_output:
            self.assertEqual(type(rect), Rectangle)
            self.assertTrue(isinstance(rect, Rectangle))

        self.assertFalse(list_rectangles_input is list_rectangles_output)
        self.assertFalse(list_rectangles_input[0] is list_rectangles_output[0])

        # Test for Square Class
        self.s1 = Square(5)
        self.s2 = Square(7, 9, 1)

        list_squares_input = [self.s1, self.s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file_csv()

        self.assertTrue(type(list_squares_output) == list)

        for square in list_squares_input:
            self.assertEqual(type(square), Square)
            self.assertTrue(isinstance(square, Square))

        self.assertFalse(list_squares_input is list_squares_output)
        self.assertFalse(list_squares_input[0] is list_squares_output[0])
