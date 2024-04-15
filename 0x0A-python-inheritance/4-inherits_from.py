#!/usr/bin/python3


def inherits_from(obj, a_class):
    """
    Checks if an obj is a sub_class of a_class.
    Args:
        obj: The obj
        a_class: The sub_class.
    Returns:
        Boolean.
    """
    is_sub = issubclass(type(obj), a_class) and type(obj) is not a_class
    return is_sub
