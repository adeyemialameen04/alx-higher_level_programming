#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff_set_1 = set_1 - set_2
    diff_set_2 = set_2 - set_1

    new_set = diff_set_1 | diff_set_2

    return new_set
