#!/usr/bin/env python3
import numpy as np
def add_arrays(arr1, arr2):
    """Calculates the element-wise addition of two arrays"""
    if len(arr1) != len(arr2):
        return None
    else:
        add_arrays = np.add(arr1, arr2)
    return add_arrays