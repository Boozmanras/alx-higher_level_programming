#!/usr/bin/python3
"""
Module for matrix multiplication using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy
    """
    try:
        result = np.matmul(m_a, m_b)
        return result.tolist()
    except Exception as e:
        raise ValueError("m_a and m_b can't be multiplied")
