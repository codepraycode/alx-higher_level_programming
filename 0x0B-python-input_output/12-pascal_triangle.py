#!/usr/bin/python3
"""Function that returns a list of lists of integers
representing the Pascal's triangle of n

    Prototype: def pascal_triangle(n)
        Args:
            n(int): int parameter
"""


def pascal_triangle(n):
    """Function that returns a list of lists of integers
    representing the Pascal's triangle of n using recurssion.

    Args:
        n(int): int parameter
    """

    if n <= 0:
        return []

    _triangle = [[1]]

    while True:
        if len(_triangle) == n:
            break

        _base = _triangle[-1]
        _new_base = [1, 1]

        if len(_base) > 1:
            for ee in range(1, len(_base)):
                _sum = _base[ee - 1] + _base[ee]
                _new_base.insert(-1, _sum)

        _triangle.append(_new_base)
    
    return _triangle
