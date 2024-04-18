#!/usr/bin/python3
"""Documenting module"""
from base import Base


class Rectangle(Base):
    """
    A rectangle class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new rectangle class.
        Args:
            width: The width.
            height: The height.
            x: X val.
            y: Y val.
            id: Id of the rec.
        """
        super.__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def x(self):
        """
        X property getter
        Returns:
            The value.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the X value.
        Args:
            value: The new value
        Returns:
            Nothing.
        """
        self.__x = value

    @property
    def y(self):
        """
        Y property getter
        Returns:
            The Y value.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the y value.
        Args:
            value: The new value
        Returns:
            Nothing.
        """
        self.__y = value

    @property
    def height(self):
        """
        Height property getter
        Returns:
            The height value.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height value.
        Args:
            value: The new value
        Returns:
            Nothing.
        """
        self.__height = value

    @property
    def width(self):
        """
        Width property getter
        Returns:
            The width value.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width value.
        Args:
            value: The new value
        Returns:
            Nothing.
        """
        self.__width = value
