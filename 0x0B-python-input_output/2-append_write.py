#!/usr/bin/python3
"""Documenting module"""


def append_write(filename="", text=""):
    """
    Appends to a file.
    Args:
        filename: The file to append to
        text: The text to append.
    Returns:
        Nothing
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
