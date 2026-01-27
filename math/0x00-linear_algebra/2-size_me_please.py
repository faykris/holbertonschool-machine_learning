#!/usr/bin/env python3
"""
2. Size Me Please
"""


def recursive_shape(matrix, shape):
    """Return shape with recursion"""
    try:
        shape.append(len(matrix))
        return recursive_shape(matrix[0], shape)
    except TypeError:
        return shape


def matrix_shape(matrix):
    """size of the matrix"""
    return recursive_shape(matrix, [])

