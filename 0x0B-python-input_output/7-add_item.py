#!/usr/bin/python3
"""Documenting module"""
import json
import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
if not path.exists(filename):
    save_to_json_file([], filename)
items = load_from_json_file(filename)

for i in range(1, len(sys.argv)):
    items.append(sys.argv[i])

save_to_json_file(items, filename)
