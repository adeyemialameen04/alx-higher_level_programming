#!/usr/bin/python3
"""
Matrix multiply
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices
    Args:
        m_a: The first matrix.
        m_b: The second matrix.
    Returns:
        The product.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if len(row) == 0:
            raise ValueError("m_a can't be empty")

    for row in m_b:
        if len(row) == 0:
            raise ValueError("m_b can't be empty")

    if not all(isinstance(element, (int, float))
               for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(isinstance(element, (int, float))
               for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    a = np.array(m_a)
    b = np.array(m_b)

    try:
        result = np.dot(a, b)
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e

    return result
