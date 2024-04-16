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

    def to_json(self, attrs=None):
        """
        Turns a student class to obj.
        Returns:
            A obj rep of the class.
        """
        new_dict = {}
        if attrs is None:
            return self.__dict__
        for item in attrs:
            if item in self.__dict__.keys():
                new_dict[item] = self.__dict__.get(item)
        return new_dict

    def reload_from_json(self, json):
        """
        Sets all the attrs of the Student to the one in the json
        Args:
            json: The json
        Returns:
            Nothing.
        """
        for key, value in json.items():
            setattr(self, key, value)
