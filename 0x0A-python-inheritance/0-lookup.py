#!/usr/bin/python3
"""Documenting module"""


def lookup(obj):
    """
    Returns all the avialable methods and attributes of an obj.
    Args:
        obj: The obejct
    Returns:
        Al list of sttr and methods.
    """
    return dir(obj)
