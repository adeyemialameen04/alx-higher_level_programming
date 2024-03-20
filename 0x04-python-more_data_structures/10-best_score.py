#!/usr/bin/python3

def best_score(a_dictionary):
    scores = []
    max_key = ""

    if a_dictionary is None:
        return None

    for key, value in a_dictionary.items():
        scores.append(value)
    max_num = scores[0]

    for num in scores:
        if num > max_num:
            max_num = num

    for key, value in a_dictionary.items():
        if max_num == value:
            max_key = key

    return max_key
