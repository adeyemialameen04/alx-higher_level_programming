#!/usr/bin/python3
"""Documenting module"""
import json


def from_json_string(my_str):
    """
    Turn json to obj.
    Args:
        my_str: The obj to be turned.
    Returns:
        Nothing
    """
    data = json.loads(my_str)
    return data
