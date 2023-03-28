#!/usr/bin/python3
"""
    Square class with a size
"""


class Square(object):
    """
        A Square class to be instantiated with a size
    """

    def __init__(self, size=0):
        """
            Initializing class and constructing square

            Note:
                - size must be an integer, else a TypeError is raised with a message.
                - size must be greater than 0, else a ValueError is raised with a message.

            Args:
                size(int, optional): The size of square to be constructed
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
        self.__size = size
