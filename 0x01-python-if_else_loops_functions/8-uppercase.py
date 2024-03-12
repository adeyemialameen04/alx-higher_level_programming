#!/usr/bin/python3

def uppercase(s):
    length = len(s)

    for i, char in enumerate(s):
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(uppercase_char), end='' if i < length - 1 else '\n')
        else:
            print("{}".format(char), end='' if i < length - 1 else '\n')
