#!/usr/bin/python3
"""Documenting module"""


def class_to_json(obj):
    """
    Turns a class to obj.
    Args:
        obj: The class to be jurned
    Returns:
        Nothing
    """
    return obj.__dict__
