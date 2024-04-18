#!/usr/bin/python3
"""Documenting module"""


class Base:
    """
    Base class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialises id.
        Args:
            id: The id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb__objects += 1
            self.id = Base.__nb_objects
