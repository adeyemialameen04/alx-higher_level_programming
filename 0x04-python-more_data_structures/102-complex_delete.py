#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys_to_delete = []
    for key_dict, val_dict in a_dictionary.items():
        if value == val_dict:
            keys_to_delete.append(key_dict)

    for key in keys_to_delete:
        del a_dictionary[key]

    return a_dictionary
