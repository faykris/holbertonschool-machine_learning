#!/usr/bin/env python3
"""
2. Size Me Please
"""


def matrix_shape(matrix):
    """size of the matrix"""
    if not isinstance(matrix, list):
        return []
    return [len(matrix)] + matrix_shape(matrix[0])

