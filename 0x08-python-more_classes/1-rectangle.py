#!/usr/bin/python3
"""
Empty rectangle.
"""


class Rectangle:
    """
    Empty rectangle class.
    """
    def __init__(self, width=0, height=0):
        """
        Sets the height and width when a new class is created
        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        # if not isinstance(width, int):
        #     raise TypeError("width must be an integer")
        # elif width < 0:
        #     raise TypeError("width must be >= 0")
        # else:
        #     self.__width = width
        #
        # if not isinstance(height, int):
        #     raise TypeError("height must be an integer")
        # elif height < 0:
        #     raise TypeError("height must be >= 0")
        # else:
        #     self.__height = height
        self.__width = width
        self.__height = height

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
            raise TypeError("width must be >= 0")
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
            raise TypeError("height must be >= 0")
        self.__height = value
