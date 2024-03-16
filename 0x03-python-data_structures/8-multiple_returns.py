#!/usr/bin/python3

def multiple_returns(sentence):
    first_char = ""
    str_len = len(sentence)
    if str_len == 0:
        first_char = None
    else:
        first_char = sentence[:1]

    new_tuple = (str_len, first_char)
    return new_tuple
