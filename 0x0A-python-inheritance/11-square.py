#!/usr/bin/python3
"""Documenting module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square.
    """
    def __init__(self, size):
        """
        Init class square.
        Args:
            size: The height and width of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
