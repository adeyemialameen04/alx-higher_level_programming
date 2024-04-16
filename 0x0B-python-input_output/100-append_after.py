#!/usr/bin/python3
"""Documenting a module"""


def append_after(filename="", search_string="", new_string=""):
    tmp = ""
    with open(filename, "r") as file:
        for line in file:
            tmp += line
            if search_string in line:
                tmp += new_string

    with open(filename, "w") as file:
        file.write(tmp)
