#!/usr/bin/python3
"""Documenting module"""
import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        print('{}'.format(resp.info().get('X-Request-id')))
