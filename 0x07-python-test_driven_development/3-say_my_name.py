#!/usr/bin/python3
"""
Say my name module.
Function name:-> say_my_name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the first name and last name.
    Args:
        first_name: A string of the first name.
        last_name: A string of the last name.
    Returns:
        Nothing.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
