#!/usr/bin/env python3
"""
2. Size Me Please
"""


def recursive_shape(matrix, shape):
    """Return shape with recursion"""
    if list is type(matrix):
        shape.append(len(matrix))
        return recursive_shape(matrix[0], shape)
    return shape


def matrix_shape(matrix):
    """size of the matrix"""
    return recursive_shape(matrix, [])

