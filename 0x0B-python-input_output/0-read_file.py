#!/usr/bin/python3
"""Documenting module"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        data = file.read()
        print(data)
