
#!/usr/bin/python3
"""This module define a test suite"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangle(unittest.TestCase):
    """This class defines series test suite"""

    def setUp(self):
        """This method creates Rectangle class instances"""

        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(10, 2, 0, 0, 12)
        self.r4 = Rectangle(10, 2, 2, 3)
        self.r33 = Rectangle(10, 2, 6)

    def tearDown(self):
        """This method resets class attribute to 0 so that
        new instances can have non-incremental values for
        their id attributes
        """

        Base._Base__nb_objects = 0

    def test_class_type(self):
        """The method checks whether object instance
        was created correctly
        """

        self.assertEqual(self.r1.__class__.__name__, "Rectangle")
        self.assertEqual(type(self.r1), Rectangle)
        self.assertIsInstance(self.r1, Rectangle)
        self.assertIsInstance(self.r1, Base)

    def test_inheritance(self):
        """This method tests for inheritance"""

        self.assertTrue(issubclass(Rectangle, Base))

    def test_attribute(self):
        """Test to ensure attribute is correctly instantiated"""

        self.assertTrue(hasattr(self.r1, 'id'))
        self.assertTrue(hasattr(self.r1, 'width'))
        self.assertTrue(hasattr(self.r1, 'height'))
        self.assertTrue(hasattr(self.r1, 'x'))
        self.assertTrue(hasattr(self.r1, 'y'))
        # self.assertTrue(hasattr(self.r1, 'y'))

    def test_unique_attribute_values(self):
        """The method tests if unique id' are created for each instance"""

        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r1.y, 0)

    def test_custom_attribute_values(self):
        """This method tests if instances have a custom id when id is not
        None"""

        self.assertEqual(self.r4.id, 3)
        self.assertEqual(self.r4.x, 2)
        self.assertEqual(self.r4.y, 3)
        self.assertEqual(self.r4.x, 2)
        self.assertEqual(self.r4.y, 3)

    def test_incremental_id(self):
        """This method tests if the id attribute is incremented correctly"""

        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r3.id, 12)
        self.assertNotEqual(self.r4.id, 12)

    def test_input_validation(self):
        """This method tests for valid inputs during class instantiation"""

        # Test suite for TypeError
        with self.assertRaises(TypeError):
            self.r5 = Rectangle(1.035, 2)
        with self.assertRaises(TypeError):
            self.r5 = Rectangle(3.5, 2)
        with self.assertRaises(TypeError):
            self.r6 = Rectangle(15, "equere")
        with self.assertRaises(TypeError):
            self.r7 = Rectangle(15, 16.9)
        with self.assertRaises(TypeError):
            self.r8 = Rectangle(15.0, 16.9)
        with self.assertRaises(TypeError):
            self.r9 = Rectangle("ifiok", "equere")
        with self.assertRaises(TypeError):
            self.r10 = Rectangle("1", 2)
        with self.assertRaises(TypeError):
            self.r11 = Rectangle(8, "2")
        with self.assertRaises(TypeError):
            self.r12 = Rectangle("0", "0")
        with self.assertRaises(TypeError):
            self.r13 = Rectangle()
        with self.assertRaises(TypeError):
            self.r14 = Rectangle(3, 2, "2", 3)
        with self.assertRaises(TypeError):
            self.r15 = Rectangle(3, 2, 2, "3")
        with self.assertRaises(TypeError):
            self.r16 = Rectangle(3, 2, "2", "3")
        with self.assertRaises(TypeError):
            self.r17 = Rectangle(3, 2, "2", "3")
        with self.assertRaises(TypeError):
            self.r30 = Rectangle(5, 6, None, -3, 7)
        with self.assertRaises(TypeError):
            self.r31 = Rectangle(5, 6, [2])
        with self.assertRaises(TypeError):
            self.r32 = Rectangle(5, 6, {}, 4)
        with self.assertRaises(TypeError):
            self.r34 = Rectangle("", 6, "", 4)
        with self.assertRaises(TypeError):
            self.r35 = Rectangle("", 6, 7, 54)
        with self.assertRaises(TypeError):
            self.r36 = Rectangle(5, 6, 7, "")
        with self.assertRaises(TypeError):
            self.r37 = Rectangle(None, 6, 7, 3)
        with self.assertRaises(TypeError):
            self.r38 = Rectangle(1, None, 7, 0)
        with self.assertRaises(TypeError):
            self.r40 = Rectangle(1)

        # Test suite for ValueError
        with self.assertRaises(ValueError):
            self.r18 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            self.r19 = Rectangle(1, -2)
        with self.assertRaises(ValueError):
            self.r20 = Rectangle(-1, -2)
        with self.assertRaises(ValueError):
            self.r21 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            self.r22 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            self.r23 = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            self.r24 = Rectangle(5, -6, 0, 3, 7)
        with self.assertRaises(ValueError):
            self.r25 = Rectangle(5, 6, -4, 0, 0)
        with self.assertRaises(ValueError):
            self.r26 = Rectangle(-5, -6, -4, -1)
        with self.assertRaises(ValueError):
            self.r27 = Rectangle(5, 6, -1, 3, 7)
        with self.assertRaises(ValueError):
            self.r28 = Rectangle(5, 6, 8, -5)
        with self.assertRaises(ValueError):
            self.r29 = Rectangle(5, 6, -2, -3, 7)

        try:
            self.r = Rectangle(10, "2")
        except Exception as e:
            self.assertEqual(str(e), "height must be an integer")

        try:
            self.r = Rectangle(10, 2)
            self.r.width = -10
        except Exception as e:
            self.assertTrue(str(e) == "width must be > 0")

        try:
            self.r = Rectangle(10, 2)
            self.r.x = {}
        except Exception as e:
            self.assertTrue(str(e) == "x must be an integer")

        try:
            self.r = Rectangle(10, 2, 3, -1)
        except Exception as e:
            self.assertTrue(str(e) == "y must be >= 0")

    def test_area(self):
        """This method tests for correctness of computed rectangle area"""

        self.r1 = Rectangle(3, 2)
        self.assertEqual(self.r1.area(), 6)

        self.r2 = Rectangle(2, 10)
        self.assertEqual(self.r2.area(), 20)

        self.r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(self.r3.area(), 56)

    def test_display(self):
        """Test for correct rectangle display"""

        # Reset class variable _nd_instance so id count is not affected
        # with new instance creation
        self.tearDown()

        self.r1 = Rectangle(4, 6)
        self.r2 = Rectangle(2, 2)
        self.r3 = Rectangle(6, 4)

        # Test for r1 instance
        # create StringIO object
        std_out_capture = StringIO()
        # re-direct stdout to StringIO object
        sys.stdout = std_out_capture
        # call method to print to stdout (i.e to StringIO object)
        self.r1.display()
        # store stdout in a variable after stripping trailing newline character
        printed_output = std_out_capture.getvalue().rstrip('\n')
        # output to be tested against
        expected_output = "####\n####\n####\n####\n####\n####"
        self.assertEqual(printed_output, expected_output)

        # Test for r2 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        self.r2.display()
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "##\n##"
        self.assertEqual(printed_output, expected_output)

        # Test for r3 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        self.r3.display()
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "######\n######\n######\n######"
        self.assertEqual(printed_output, expected_output)

        # reset stdout to terminal output
        sys.stdout = sys.__stdout__

    def test_str(self):
        """This method tests for the unofficial string rep of the rectangle
        object
        """

        # Reset class variable _nd_instance so id count is not affected
        # with new instance creation
        self.tearDown()

        self.r40 = Rectangle(4, 6, 2, 1, 12)
        self.r41 = Rectangle(5, 5, 1)
        self.r42 = Rectangle(7, 6)

        # Test for r1 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r40)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(printed_output, expected_output)

        # Test for r2 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r41)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(printed_output, expected_output)

        # Test for r3 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r42)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (2) 0/0 - 7/6"
        self.assertEqual(printed_output, expected_output)

        # reset stdout to terminal output
        sys.stdout = sys.__stdout__

    def test_dispay_updated(self):
        """This method tests for the updated rectangle display method
        """

        # Reset class variable _nd_instance so id count is not affected
        # with new instance creation
        self.tearDown()

        self.r1 = Rectangle(2, 3, 2, 2)
        self.r2 = Rectangle(3, 2, 1, 0)
        self.r3 = Rectangle(2, 3)
        self.r4 = Rectangle(3, 2, 0, 2)
        self.r5 = Rectangle(3, 2, 2)

        # Test for r1 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        self.r1.display()
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "\n\n  ##\n  ##\n  ##"
        self.assertEqual(printed_output, expected_output)

        # Test for r2 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        self.r2.display()
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = " ###\n ###"
        self.assertEqual(printed_output, expected_output)

        # Test for r3 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        self.r3.display()
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "##\n##\n##"
        self.assertEqual(printed_output, expected_output)

        # Test for r4 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        self.r4.display()
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "\n\n###\n###"
        self.assertEqual(printed_output, expected_output)

        # Test for r5 instance
        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        self.r5.display()
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "  ###\n  ###"
        self.assertEqual(printed_output, expected_output)

        # reset stdout to terminal output
        sys.stdout = sys.__stdout__

    def test_update(self):
        """Tests for the update method"""

        self.tearDown()

        self.r1 = Rectangle(10, 10, 10, 10)

        # Test for r1 instance

        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r1.x, 10)
        self.assertEqual(self.r1.y, 10)

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r1)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (1) 10/10 - 10/10"
        self.assertEqual(printed_output, expected_output)

        # Test for 1st update

        self.r1.update(89)

        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r1.x, 10)
        self.assertEqual(self.r1.y, 10)

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r1)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(printed_output, expected_output)

        # Test for 2nd update

        self.r1.update(89, 2)

        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r1.x, 10)
        self.assertEqual(self.r1.y, 10)

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r1)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (89) 10/10 - 2/10"
        self.assertEqual(printed_output, expected_output)

        # Test for 3rd update

        self.r1.update(89, 2, 3)

        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 10)
        self.assertEqual(self.r1.y, 10)

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r1)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (89) 10/10 - 2/3"
        self.assertEqual(printed_output, expected_output)

        # Test for 4th update

        self.r1.update(89, 2, 3, 4)

        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r1.y, 10)

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r1)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (89) 4/10 - 2/3"
        self.assertEqual(printed_output, expected_output)

        # Test for 5th update

        self.r1.update(89, 2, 3, 4, 5)

        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r1.y, 5)

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r1)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(printed_output, expected_output)

        # reset stdout to terminal output
        sys.stdout = sys.__stdout__

    def test_update_2(self):
        """Additional tests for added functionality to the update method"""

        self.tearDown()

        # Test for r1
        self.r1 = Rectangle(10, 10, 10, 10)

        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r1.x, 10)
        self.assertEqual(self.r1.y, 10)

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r1)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (1) 10/10 - 10/10"
        self.assertEqual(printed_output, expected_output)

        # Test for 1st update
        self.r1.update(height=1)

        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r1.height, 1)
        self.assertEqual(self.r1.x, 10)
        self.assertEqual(self.r1.y, 10)

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r1)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (1) 10/10 - 10/1"
        self.assertEqual(printed_output, expected_output)

        # Test for 2nd update
        self.r1.update(width=1, x=2)

        self.assertEqual(self.r1.id, 1)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 1)
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r1.y, 10)

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r1)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (1) 2/10 - 1/1"
        self.assertEqual(printed_output, expected_output)

        # Test for 3rd update
        self.r1.update(y=1, width=2, x=3, id=89)

        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 1)
        self.assertEqual(self.r1.x, 3)
        self.assertEqual(self.r1.y, 1)

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r1)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (89) 3/1 - 2/1"
        self.assertEqual(printed_output, expected_output)

        # Test for 4th update
        self.r1.update(x=1, height=2, y=3, width=4)

        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.width, 4)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r1.x, 1)
        self.assertEqual(self.r1.y, 3)

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r1)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (89) 1/3 - 4/2"
        self.assertEqual(printed_output, expected_output)

        # reset stdout to terminal output
        sys.stdout = sys.__stdout__

    def test_to_dictionary(self):
        """Test for dictionary representation of Square class"""

        self.tearDown()

        self.r1 = Rectangle(10, 2, 1, 9)
        self.r1_dictionary = self.r1.to_dictionary()

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r1)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (1) 1/9 - 10/2"
        self.assertEqual(printed_output, expected_output)

        self.assertTrue(type(self.r1_dictionary), "dict")

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r1_dictionary)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}"
        self.assertEqual(printed_output, expected_output)

        self.r2 = Rectangle(1, 1)
        self.assertEqual(self.r2.id, 2)
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r2.height, 1)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r2.y, 0)

        self.r2.update(**self.r1_dictionary)
        self.assertEqual(self.r2.id, 1)
        self.assertEqual(self.r2.width, 10)
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r2.x, 1)
        self.assertEqual(self.r2.y, 9)

        std_out_capture = StringIO()
        sys.stdout = std_out_capture
        print(self.r2)
        printed_output = std_out_capture.getvalue().rstrip('\n')
        expected_output = "[Rectangle] (1) 1/9 - 10/2"
        self.assertEqual(printed_output, expected_output)

        self.assertFalse(self.r1 == self.r2)
