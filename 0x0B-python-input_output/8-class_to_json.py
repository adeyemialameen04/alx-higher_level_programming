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
    # json_str = json.dumps(obj.__dict__)
    # obj_str = json.loads(json_str)
    return obj.__dict__
