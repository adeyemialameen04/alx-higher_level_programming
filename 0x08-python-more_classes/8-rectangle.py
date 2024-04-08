#!/usr/bin/python3
"""
Empty rectangle.
"""


class Rectangle:
    """
    Empty rectangle class.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Sets the height and width when a new class is created
        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        Rectangle.number_of_instances += 1
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """
        Gets the width value.
        Returns:
            The width
        """
        return self.__width

    @property
    def height(self):
        """
        Gets the height property.
        Returns:
            The height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets the value of the width to value.
        Args:
            value: The value it's going to be set to.
        Returns:
            Nothing.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the value of height to value.
        Args:
            value: The value it's going to be set to
        Returns:
            Nothing.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """
        Prints # based on the height and width of the rectangle.
        Returns:
            Multiple #
        """
        if self.__height == 0 or self.__height == 0:
            return ""

        rec_str = ""
        for _ in range(self.__height):
            rec_str += str(self.print_symbol) * self.__width + '\n'
        return rec_str.rstrip()

    def __repr__(self):
        """
        Prints strig represntation of rectangle.
        Returns:
            The string representation.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2
        if rect_1.area() == rect_2.area():
            return rect_1
