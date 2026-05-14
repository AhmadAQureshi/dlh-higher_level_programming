#!/usr/bin/env python3
import numpy as np
def cat_arrays(arr1, arr2):
    """Concatenates two arrays"""
    cat_arrays = np.concatenate((arr1, arr2))
    return cat_arrays