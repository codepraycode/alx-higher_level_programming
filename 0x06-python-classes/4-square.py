#!/usr/bin/python3
"""Square class with a size"""

class Square(object):
    """A Square class to be instantiated with a size"""

    def __init__(self, size=0):
        """Initializing class and constructing square

        Note:
            - size must be an integer, else a TypeError is raised.
            - size must be greater than 0, else a ValueError is raised.

        Args:
            size(int, optional): The size of square to be constructed

        Raises:
            TypeError: if `size` is an integer.
            ValueError: if `size` is less than 0.
        """
        self.__set_size(size)

    def area(self):
        """Square area method

        Calculate the area of the square instance

        Returns:
            int: current area of the square instance

        """
        return self.__size ** 2

    def __set_size(self, value):
        """Validates and update the size of square"""

        # Validate value is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # Validate value is greater than 0
        if value < 0:
            raise TypeError("size must be >= 0")

        #: int: private class attribute
        self.__size = value

    @property
    def size(self):
        """str: size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size of Square instance

        Args:
            value(int): The new size of square

        Raises:
            TypeError: if `size` is an integer.
            ValueError: if `size` is less than 0.
        """
        self.__set_size(value)
