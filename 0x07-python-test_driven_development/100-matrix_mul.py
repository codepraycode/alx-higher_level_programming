#!/usr/bin/python3
"""Function that multiplies 2 matrices
    Prototye: def matrix_mul(m_a, m_b)

        Args:
            m_a(list): List of lists of intergers/floats`
            m_b(list): List of lists of intergers/floats`

        Raises:
            TypeError: There are differenct cases
                case1a: if m_a is not a list
                    expected message should be: `m_a must be a list`
                case1b: if m_b is not a list
                    expected message should be: `m_b must be a list`
                case2a: if m_a is not a list of lists
                    expected message should be: `m_a must be a list of lists`
                case2b: if m_b is not a list of lists
                    expected message should be: `m_b must be a list of lists`
                case3a: if one element of m_a list of lists is not integer/float
                    expected message should be: `m_a should contain only integers or floats`
                case3b: if one element of m_b list of lists is not integer/float
                    expected message should be: `m_b should contain only integers or floats`
                case4a: if m_a is not a rectangle (i.e all rows should be of the same length)
                    expected message should be: `each row of m_a must be of the same size`
                case4b: if m_b is not a rectangle (i.e all rows should be of the same length)
                    expected message should be: `each row of m_b must be of the same size`
                
            ValueError: There are differenct cases
                case 1a: if m_a is an empty list (i.e [] or [[]])
                    expected message should be: `m_a can't be empty`
                case 1b: if m_b is an empty list (i.e [] or [[]])
                    expected message should be: `m_b can't be empty`
                case 2: If m_a and m_b can't be multiplied:
                    expected message should be: `m_a and m_b can't be multiplied`

        Returns:
            list: List of lists of integers/float of matrix `m_a` and `m_b`
                under the operation of martix multiplication
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices and return result of the operation
        matrices `m_a` and `m_b`

    Args:
        m_a(list): List of lists of intergers/floats`
        m_b(list): List of lists of intergers/floats`

    Raises:
        TypeError: There are differenct cases
            case1a: if m_a is not a list
                expected message should be: `m_a must be a list`
            case1b: if m_b is not a list
                expected message should be: `m_b must be a list`

            case2a: if m_a is not a list of lists
                expected message should be: `m_a must be a list of lists`
            case2b: if m_b is not a list of lists
                expected message should be: `m_b must be a list of lists`

            case3a: if one element of m_a list of lists is not integer/float
                expected message should be: `m_a should contain only integers or floats`
            case3b: if one element of m_b list of lists is not integer/float
                expected message should be: `m_b should contain only integers or floats`

            case4a: if m_a is not a rectangle (i.e all rows should be of the same length)
                expected message should be: `each row of m_a must be of the same size`
            case4b: if m_b is not a rectangle (i.e all rows should be of the same length)
                expected message should be: `each row of m_b must be of the same size`
            
        ValueError: There are differenct cases
            case 1a: if m_a is an empty list (i.e [] or [[]])
                expected message should be: `m_a can't be empty`
            case 1b: if m_b is an empty list (i.e [] or [[]])
                expected message should be: `m_b can't be empty`
            case 2: If m_a and m_b can't be multiplied:
                expected message should be: `m_a and m_b can't be multiplied`

    Returns:
        list: List of lists of integers/float of matrix `m_a` and `m_b`
            under the operation of martix multiplication
    """

    # ======== TypeErrors ========
    # Case 1a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    # Case 1b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    for row in m_a:
        # Case 2a
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        # Case 3a
        if not all(isinstance(value, (int, float)) for value in row):
            raise TypeError("m_a should contain only integers or floats")
        # Case 4a
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
            
    for row in m_b:
        # Case 2b
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        # Case 3b
        if not all(isinstance(value, (int, float)) for value in row):
            raise TypeError("m_b should contain only integers or floats")
        # Case 4b
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    
    # ========= Check for ValueErrors ===============
    # Case 1a
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    # Case 1b
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # length of elements in a row
    _m_a_cols__length = len(m_a[0])
    _m_a_rows__length = len(m_a)

    # length of all rows
    _m_b_cols__length = len(m_b[0])
    _m_b_rows__length = len(m_b)
    
    # Case 2
    # A matrix is mutiplicable if of same dimension
    if _m_a_cols__length != _m_b_rows__length:
        raise ValueError("m_a and m_b can't be multiplied")
    # ========= DONE WITH THE ERRORS ===============

    _product = [[0 for x in range(_m_b_cols__length)] for y in range(_m_a_rows__length)]

    for each_row_i in range(_m_a_rows__length): # loop through by index
        _b_col = 0

        while (_b_col < _m_b_cols__length):
            _sum = 0

            for each_col in range(len(m_a[each_row_i])):
                _sum += m_a[each_row_i][each_col] * m_b[each_col][_b_col]

            _product[each_row_i][_b_col] = _sum
            _b_col += 1
    return _product
