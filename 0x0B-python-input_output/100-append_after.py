#!/usr/bin/python3
"""Documenting a module"""


def append_after(filename="", search_string="", new_string=""):
    """
    Append after the search_string.
    Args:
        filename: The filename
        search_string: The str we are looking for
        new_string: The new_string to add.
    Returns:
        Nothing.
    """
    tmp = ""
    with open(filename, "r") as file:
        for line in file:
            tmp += line
            if search_string in line:
                tmp += new_string

    with open(filename, "w") as file:
        file.write(tmp)
