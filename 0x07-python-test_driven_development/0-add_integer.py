#!/usr/bin/python3
"""Function to add integers
    Prototye: def add_integer(a, b=98)

        Args:
            a(int, float): First integer
            b(int, float, optional): second integer

        Raises:
            TypeError: if a or b is not an integer or float
                expected message should be:
                `a must be an integer` or `b must be an integer`

        Returns:
            int: the addition of given arguments
"""


def add_integer(a, b=98):
    """Add two integers

    Args:
        a(int, float): First integer
        b(int, float, optional): second integer, defaults to 98

    Raises:
        TypeError: if a or b is not an integer or float
            expected message should be:
            `a must be an integer` or `b must be an integer`

    Returns:
        int: the addition of given arguments
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast arguments to integers
    a = int(a)
    b = int(b)

    return a + b
