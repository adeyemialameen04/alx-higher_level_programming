#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Print each element in the row with proper formatting
        print(" ".join("{:d}".format(element) for element in row))
