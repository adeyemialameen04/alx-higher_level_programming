#!/usr/bin/python3
"""Documenting module"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    r_json = r.json()
    if r_json == {}:
        print("None")
    else:
        print("{}".format(r_json.get('id')))
