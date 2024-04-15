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
    if hasattr(obj, name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
