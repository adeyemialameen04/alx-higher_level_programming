#!/usr/bin/python3
"""Documenting module"""


def magic_string():
    """
    Prints a string.
    Returns:
        Nothing.
    """
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return "BestSchool" + ", BestSchool" * (magic_string.n - 1)
