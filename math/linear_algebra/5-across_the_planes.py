#!/usr/bin/env python3
import numpy as np
def add_matrices2D(mat1, mat2):
    """Calculates the element-wise addition of two 2D matrices"""
    if len(mat1[0]) != len(mat2[0]):
        return None
    else:
        add_matrices2D = np.add(mat1, mat2)
    return add_matrices2D