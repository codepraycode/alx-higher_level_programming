#!/usr/bin/python3
"""MyInt class (subclass of int)"""


class MyInt(int):
    """MyInt that inherit from `int` class with
    extra functionalities.
    """

    def __eq__(self, n):
        """Inverting == operation
        Args:
            n(int): other operand
        """
        super().__ne__(n)

    def __nq__(self, n):
        """Inverting != operation
        Args:
            n(int): other operand
        """
        super().__eq__(n)
