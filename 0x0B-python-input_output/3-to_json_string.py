#!/usr/bin/python3
"""Documenting module"""
import json


def to_json_string(my_obj):
    """
    Turn obj to json.
    Args:
        my_obj: The obj to be turned.
    Returns:
        Nothing
    """
    data = json.dumps(my_obj)
    return data
