#!/usr/bin/python3
"""Documenting module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Documenting class.
    """
    def __init__(self, width, height):
        """
        Initializes the height and width of a rec.
        Args:
            width: Height
            height: Width.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of a rec.
        Returns:
            The area.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        prints a str rep for the rec.
        Returns:
            A string rep.
        """
        return "[Rectangle] {} / {}".format(self.__width, self.__height)
