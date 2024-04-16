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
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
