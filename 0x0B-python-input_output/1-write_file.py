#!/usr/bin/python3
"""Documenting a module."""


def write_file(filename="", text=""):
    """
    Writes to a file.
    Args:
        filename: The name of the file.
        text: The txt to be written.
    Returns:
        The length of what was written.
    """
    with open(filename, "w") as file:
        file.write(text)
        return len(text)
