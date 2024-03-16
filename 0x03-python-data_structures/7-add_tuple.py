#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    first_element = ((tuple_a[0] if len(tuple_a) > 0 else 0) +
                     (tuple_b[0] if len(tuple_b) > 0 else 0))
    second_element = ((tuple_a[1] if len(tuple_a) > 1 else 0) +
                      (tuple_b[1] if len(tuple_b) > 1 else 0))
    new_tuple = (first_element, second_element)
    return new_tuple
