#!/usr/bin/python3
"""
Divides by matrix.
matrix_divided - Function name.
"""


def matrix_divided(matrix, div):
    """
    Retuns a new matrix with each element divided by div.
    Args:
        matrix: A list of a list of numbers
        div: The divisor.

    Returns:
        A new matrix with the elements divided.
    """
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    row_num = len(matrix[0])

    for row in matrix:
        if len(row) != row_num:
            raise TypeError("Each row of the matrix must "
                            "have the same size")
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if isinstance(div, float) and div == float('inf'):
        raise OverflowError("cannot convert float infinity to integer")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return list(map(lambda row_div: list(map(lambda x: round(x / div, 2),
                                             row_div)), matrix))
