#!/usr/bin/python3
"""Documenting module"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


argc = len(sys.argv)
argv = sys.argv
items = []

for i in range(1, argc):
    items.append(argv[i])

save_to_json_file(items, "add_item.json")
