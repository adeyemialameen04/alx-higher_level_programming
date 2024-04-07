#!/usr/bin/python3
"""
Printing a square
Function name:-> print_square.
"""


def print_square(size):
    """
    Prints a square.
    Args:
        size: The size of the square to be printed.

    Returns:
        Nothing.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
