#!/usr/bin/python3
"""Documenting module"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w") as file:
        data = json.dumps(my_obj)
        file.write(data)
