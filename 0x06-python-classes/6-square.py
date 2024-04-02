#!/usr/bin/python3
"""
THis module defines a class square and gives it a size.
"""


class Square:
    """
    Defines a square.

    Attributes:
        __size (int): The size of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square object.
        Args:
            size (int): The size of the square.
            position (tuple): The coord of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """
        TO calculate the area of the square.
        Returns:
            The area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        To get the size of the square.
        Returns:
            The size of the square.
        """
        return self.__size

    @property
    def position(self):
        """
        Gets position.
        Returns:
            Postion.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of a square.
        Args:
            value (tuple): The value w want to set the position to.
        """
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        Args:
            value (int): The size of the square

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        Prints a square.
        Returns:
            Nothing.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)
