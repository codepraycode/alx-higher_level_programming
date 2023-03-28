#!/usr/bin/python3
"""Square class with a size"""


class Square(object):
    """A Square class"""

    def __init__(self, size=0, position=(0, 0)):
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
        # validate and set the inititalization parameters.
        self.__set_size(size)
        self.__set_position(position)

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

    def __set_position(self, value):
        """Validates and update the position of square"""
        #: str: default message for exception
        msg = "position must be a tuple of 2 positive integers"

        # Validate value is a tuple
        if not isinstance(value, tuple):
            raise TypeError(msg)

        # Validate value has two element
        if len(value) != 2:
            raise TypeError(msg)

        # Validate each elements in value is int
        if not all(isinstance(each, int) for each in value):
            raise TypeError(msg)

        #: int: private class attribute
        self.__position = value

    def area(self):
        """Square area method

        Calculate the area of the square instance

        Returns:
            int: current area of the square instance

        """
        return self.__size ** 2

    def my_print(self):
        """Print to stdout the square with character #

        Note:
            if `size` is 0, an empty line is printed.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def size(self):
        """int: size of square"""
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

    @property
    def position(self):
        """int: position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position of Square instance

        Args:
            value(tuple(int, int)): Tuple of two integers.

        Raises:
            TypeError: if `position` is not a tuple of two integers.
        """
        self.__set_position(value)

    def __str__(self):
        """Print the Square instance
        Display the square by printing to stdout
        """
        self.my_print()
        return ""
