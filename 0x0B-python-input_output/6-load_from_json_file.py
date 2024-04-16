#!/usr/bin/python3
"""Documenting module"""
import json


def load_from_json_file(filename):
    """
    Loads a python dict from a json file.
    Args:
        filename: aThe fiilename to be read.
    Returns:
        Nothing.
    """
    with open(filename, "r") as file:
        data = json.load(filename)
    return data
