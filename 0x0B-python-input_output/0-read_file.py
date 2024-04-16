#!/usr/bin/python3
"""Documenting module"""


def read_file(filename=""):
    """
    Reads a file and prints its data.
    Args:
        filename: The file to be read.
    Returns:
        Nothing.
    """
    with open(filename, encoding="utf-8") as file:
        data = file.read()
        print(data, end="")
