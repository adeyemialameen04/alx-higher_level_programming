#!/usr/bin/python3
"""Documenting module"""
import json


class Base:
    """
    Base class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialises id.
        Args:
            id: The id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string rep of list_dictionaries.
        Args:
            list_dictionaries: list of dicts.
        Returns:
            A JSON string repof list_dictionaries.
        """
        if not list_dictionaries:
            return "[]"
        data = json.dumps(list_dictionaries)
        return data

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_str = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, "w") as filename:
            filename.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Turns a json str to an obj.
        Args:
            json_string: The str.
        Returns:
            A list rep of json_str
        """
        if json_string is None or len(json_string) == 0:
            return "[]"

        data = json.loads(json_string)
        return data

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new class with all instances set.
        Args:
            **dictionary: like a double pointer to dict.
        Returns:
            an instance with all attributes already set
        """
        dummy = ""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        try:
            file_name = cls.__name__ + ".json"
            with open(file_name, "r") as file:
                data = file.read()
                if not data:
                    return []
                dicts = cls.from_json_string(data)
                return [cls.create(**dic) for dic in dicts]
        except FileNotFoundError:
            return []
