#!/usr/bin/python3

def uppercase(str):
    length = len(str)

    for c in str:
        if 'a' <= c <= 'z':
            upper_ch = chr(ord(c) - ord('a') + ord('A'))
            print("{}".format(upper_ch), end='' if i < length - 1 else '\n')
        else:
            print("{}".format(c), end='' if i < length - 1 else '\n')
