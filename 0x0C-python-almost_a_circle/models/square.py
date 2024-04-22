#!/usr/bin/python3
"""Documenting a module"""
from .rectangle import Rectangle


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


class Square(Rectangle):
    """
    Square class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new square class.
        Args:
            size: The height and width.
            x: The x-axis
            y: The y-axis
            id: The id of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Prints a square with '#'
        Returns:
            A str rep of the square
        """
        square_str = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                       self.width)
        return square_str

    @property
    def size(self):
        """
        Size getter
        Returns:
            The width of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Size setter
        Args:
            value: The height and width
        Returns:
            Nothing.
        """
        integer_validation("width", value)
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """
        Updates the instance of class.
        Args:
            *args: Non keyword args
            **kwargs: Keyworded args.
        Returns:
            Nothing.
        """
        if args:
            argc = len(args)
            if argc > 0:
                self.id = args[0]
            if argc > 1:
                integer_validation("width", args[1])
                self.width = args[1]
            if argc > 2:
                integer_validation("x", args[2])
                self.x = args[2]
            if argc > 3:
                integer_validation("y", args[3])
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dict of the class.
        Returns:
            A dict.
        """
        new_dict = super().to_dictionary()
        del new_dict['width']
        del new_dict['height']
        new_dict['size'] = self.size
        return new_dict
