#!/usr/bin/python3
"""Documenting a module."""


def write_file(filename="", text=""):
    with open(filename, "w") as file:
        file.write(text)
        return len(text)
