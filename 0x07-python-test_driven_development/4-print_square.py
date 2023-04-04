#!/usr/bin/python3
"""Function that prints a square with the character #.
    Prototye: def print_square(size)

        Args:
            size (int): Length of the square

        Raises:
            TypeError: There are difference cases
                case1: if size is not an integer
                    expected message should be: `size must be an integer`
                case2: if size is float and less than 0
                    expected message should be: `size must be an integer`
            ValueError: if size is less than 0
                expected message should be: `size must be >= 0`
"""


def print_square(size):
    """Prints a square with the character #.
        size of square is determined by argument `size`

    Args:
        size (int): Length of the square

    Raises:
        TypeError: There are difference cases
            case1: if size is not an integer
                expected message should be: `size must be an integer`
            case2: if size is float and less than 0
                expected message should be: `size must be an integer`
        ValueError: if size is less than 0
            expected message should be: `size must be >= 0`
    """
    # TypeErrors
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        for y in range(size):
            print("#", end='')
        print()
