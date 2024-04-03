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
    def __init__(self, size=0):
        """
        Initializes a square object.
        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        TO calculate the area of the square.
        Returns:
            The area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        To get the size of the square.
        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.
        Args:
            value (int): The size of the square

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __eq__(self, other):
        """
        Equal sign.
        Args:
            other (Square): The other square we are comapring with.

        Returns:
            True, if they are equal and False if otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Not Equal sign.
        Args:
            other (Square): The other square we are comapring with.

        Returns:
            True, if they are not equal and False if otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Greater sign.
        Args:
            other (Square): The other square we are comapring with.

        Returns:
            True, self is bigger than other and False if otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater/equal sign.
        Args:
            other (Square): The other square we are comapring with.

        Returns:
            True, self is bigger than or equal other and False if otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Less sign.
        Args:
            other (Square): The other square we are comapring with.

        Returns:
            True, self is less than other and False if otherwise.
        """

        return self.area() < other.area()

    def __le__(self, other):
        """
        Less/equal sign.
        Args:
            other (Square): The other square we are comapring with.

        Returns:
            True, self is less than or equal to other and False if otherwise.
        """
        return self.area() <= other.area()
