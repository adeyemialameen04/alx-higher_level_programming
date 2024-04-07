#!/usr/bin/python3
""" Module to add two integers or floats"""


def add_integer(a, b=98):
    """
    Returns the sum of two integers .
    Args:
        a: First argument.
        b: Second argument.

    Returns:
        The sum of a + b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
