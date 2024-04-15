#!/usr/bin/python3
"""Documenting a class"""


def add_attribute(obj, name, value):
    """
    Adds an attribute to a class.
    Args:
        obj: The class
        name: Name of the attr
        value: Value of the attr
    Returns:
        Nothing.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
