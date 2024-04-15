#!/usr/bin/python3
"""Documenting module"""


class BaseGeometry:
    """
    Documenting class.
    """
    def area(self):
        """
        Raise an exception.
        Returns:
            Nothing.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int) or type(value) == bool:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
