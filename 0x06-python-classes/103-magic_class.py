#!/usr/bin/python3
import math


class MagicClass:
    """
    MagicClass.
    """
    def __init__(self, radius=0):
        """
        Initialization.
        Args:
            radius(int, float): The radius.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        The area.
        Returns:
            Gibberish.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        The circumference.
        Returns:
            Gibberish.
        """
        return 2 * math.pi * self.__radius
