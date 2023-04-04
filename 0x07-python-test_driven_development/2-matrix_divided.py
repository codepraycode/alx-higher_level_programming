#!/usr/bin/python3
"""Function that divides all elements of a matrix.
    Prototye: def matrix_divided(matrix, div)

        Args:
            matrix ([[(int,floats)]]): List of lists of integer/float
            div (int, float): value to divide elements of matrix by

        Raises:
            TypeError: There are differenct cases
                case1: if matrix is not a list of list of integer/float
                    expected message should be:
                    `matrix must be a matrix (list of lists) of integers/floats
                case2: if each row in matrix is not of same size
                    expected message should be:
                    `Each row of the matrix must have the same size`
                case3: if div is not integer/float
                    expected message should be:
                    `div must be a number`
            ZeroDivisionError: if `div` is equal to 0
                expected message should be: `division by zero`

        Returns:
            matrix(list): List of lists of integers/float of which each elements
                has been divided by `div` and rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divide a matrix by a given number `div`

    Args:
        matrix ([[(int,floats)]]): List of lists of integer/float
        div (int, float): value to divide elements of matrix by

    Raises:
        TypeError: There are differenct cases
            case1: if matrix is not a list of list of integer/float
                expected message should be:
                `matrix must be a matrix (list of lists) of integers/floats`
            case2: if each row in matrix is not of same size
                expected message should be:
                `Each row of the matrix must have the same size`
            case3: if div is not integer/float
                expected message should be:
                `div must be a number`
        ZeroDivisionError: if `div` is equal to 0
            expected message should be: `division by zero`

    Returns:
        matrix(list): List of lists of integers/float of which each elements
            has been divided by `div` and rounded to 2 decimal places.
    """
    # ZeroDivision Error
    if div === 0:
        raise ZeroDivisionError("division by zero")

    # TypeErrors
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    first_row_size = len(matrix[0])
    new_matrix = []

    for each_row in matrix:
        if len(each_row) != first_row_size:
            raise TypeError("Each row of the matrix must have the same size")

        if not all(isinstance(value, (int, float)) for value in each_row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
        # Update new_matrix
        new_matrix += [eval("{:.2f}".format(value / div)) for value in each_row]

    return new_matrix
