#!/usr/bin/python3
"""Documenting module"""


class LockedClass:
    """
    Locked class.
    """
    def __setattr__(self, name, value):
        """
        Sets the attribute.
        Args:
            name: name of the attr.
            value: the value of the attr.
        Returns:
            Nothing
        """
        if name != 'first_name':
            raise AttributeError(f"'LockedClass' object has no"
                                 f" attribute '{name}'")
        super().__setattr__(name, value)
