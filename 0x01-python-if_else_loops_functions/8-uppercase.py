#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if 'a' <= c <= 'z':
            upper_ch = chr(ord(c) - ord('a') + ord('A'))
            print("{}".format(upper_ch), end='')
        else:
            print("{}".format(c), end='')
