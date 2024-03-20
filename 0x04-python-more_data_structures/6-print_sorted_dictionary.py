#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    for item in keys:
        print(f"{item}: {a_dictionary.get(item)}")
