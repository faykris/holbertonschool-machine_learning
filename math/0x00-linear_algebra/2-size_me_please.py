#!/usr/bin/env python3
"""
2. Size Me Please
"""


def matrix_shape(matrix):
    """size of the matrix"""
    shape = [len(matrix)]
    for i in matrix:
        if list is type(i):
            shape.append(len(i))
            for j in i:
                if list is type(j):
                    shape.append(len(j))
                break
        break
    return shape

