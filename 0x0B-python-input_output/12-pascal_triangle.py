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

        _base = _triangle[-1]  # base of triangle
        # template, all new values will be inserted in between
        _new_base = [1, 1]

        # check if it is not [1]; otherwise return [1, 1]
        if len(_base) > 1:
            # Start from second index and calculate with previous value
            for val_index in range(1, len(_base)):
                _sum = _base[val_index - 1] + _base[val_index]
                # Adds _sum value as second to the last value in _new_base
                _new_base.insert(-1, _sum)
                # continues like that till _base is exhausted

        # _new_base might not change
        #   if the previous base was [1]
        _triangle.append(_new_base)

    return _triangle
