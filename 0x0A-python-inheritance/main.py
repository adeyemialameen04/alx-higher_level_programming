#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

bg.integer_validator("my_int", 12)
bg.integer_validator("width", True)
# bg.integer_validator(20)

# >>> bg.integer_validator(20)
# Traceback (most recent call last):
# ...
# TypeError: BaseGeometry.integer_validator() missing 1 required
# positional argument: 'value'
