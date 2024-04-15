#!/usr/bin/python3
"""Documenting module"""


class MyInt(int):
    """
    Crazy class
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
