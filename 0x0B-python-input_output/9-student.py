#!/usr/bin/python3
"""Documenting module"""


class Student:
    """
    Student class.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a student class.
        Args:
            first_name: first_name
            first_name: first_name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Turns a student class to obj.
        Returns:
            A obj rep of the class.
        """
        return self.__dict__
