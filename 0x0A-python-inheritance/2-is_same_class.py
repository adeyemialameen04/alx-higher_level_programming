#!/usr/bin/python3
"""Is instance"""


def is_same_class(obj, a_class):
    """
    Checks if an object is a instance of a class.
    Args:
        obj: The obj to be checked.
        a_class: The class to check in.
    Returns:
        True if yes and flase otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
