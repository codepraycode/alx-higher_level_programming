#!/usr/bin/python3
"""Function that multiplies 2 matrices by using the module NumPy
    Prototye: def lazy_matrix_mul(m_a, m_b):

        Args:
            m_a(list): List of lists of intergers/floats`
            m_b(list): List of lists of intergers/floats`

        Returns:
            list: martix multiplication by numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices and return result of the operation
        matrices `m_a` and `m_b`

    Args:
        m_a(list): List of lists of intergers/floats`
        m_b(list): List of lists of intergers/floats`

    Returns:
        list: martix multiplication by numpy
    """

    return np.matmul(m_a, m_b)
