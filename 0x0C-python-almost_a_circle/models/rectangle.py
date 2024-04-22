#!/usr/bin/python3
"""Documenting module"""
from .base import Base


def integer_validation(name, value):
    """
    Integer validation
    Args:
        name: The name of tyhe attr
        value: The value.
    Returns:
        Nothing
    """
    if not isinstance(value, int):
        raise TypeError("{} must be an integer".format(name))
    if (name == "width" or name == "height") and value <= 0:
        raise ValueError("{} must be > 0".format(name))
    elif (name == "x" or name == "y") and value < 0:
        raise ValueError("{} must be >= 0".format(name))


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
            id: id of the rec.
        """
        super().__init__(id)
        integer_validation("width", width)
        self.__width = width
        integer_validation("height", height)
        self.__height = height
        integer_validation("x", x)
        self.__x = x
        integer_validation("y", y)
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
        integer_validation("x", value)
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
        integer_validation("y", value)
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
        integer_validation("height", value)
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
        integer_validation("width", value)
        self.__width = value

    def area(self):
        """
        Computes the area of the rec/
        Returns:
            The height * width
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the rec in '#'.
        Returns:
            Nothing.
        """
        for y_axis in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            row_str = ""
            for x_sp in range(0, self.__x):
                row_str += " "
            for j in range(0, self.__width):
                row_str += "#"
            print(row_str)

    def __str__(self):
        """
        Prints the str representation of the rectangle.
        Returns:
            A str rep of the rec.
        """
        rec_str = ("[Rectangle] ({}) {}/{} - {}/{}"
                   .format(self.id, self.__x, self.__y,
                           self.__width, self.__height))
        return rec_str

    def update(self, *args, **kwargs):
        """
        Updates the values in the rec
        Args:
            *args: The args
        Returns:
            Nothing.
        """
        # attrs = {"width"}
        if args:
            argc = len(args)
            if argc > 0:
                self.id = args[0]
            if argc > 1:
                integer_validation("width", args[1])
                self.__width = args[1]
            if argc > 2:
                integer_validation("height", args[2])
                self.__height = args[2]
            if argc > 3:
                integer_validation("x", args[3])
                self.__x = args[3]
            if argc > 4:
                integer_validation("y", args[4])
                self.__y = args[4]

        if kwargs is not None:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dict of the class.
        Returns:
            A dict.
        """
        new_dict = {'x': self.x, 'y': self.y, 'id': self.id,
                    'height': self.height, 'width': self.width}
        return new_dict
