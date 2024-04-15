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
        Rectangle.__init__(self, size, size)
        self.__size = size
