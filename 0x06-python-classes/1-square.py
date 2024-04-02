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
    def __init__(self, size):
        """
        Initializes a square object.
        Args:
            size (int): The size of the square.
        """
        self.__size = size
