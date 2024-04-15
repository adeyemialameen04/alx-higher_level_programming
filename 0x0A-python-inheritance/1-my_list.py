#!/usr/bin/python3
"""Print sorted"""


class MyList(list):
    """
    List class.
    """
    def __init__(self):
        pass

    def print_sorted(self):
        """
        Prints a sorted list
        Returns:
            Nothing.
        """
        copy = self.copy()
        copy.sort()
        print(copy)
