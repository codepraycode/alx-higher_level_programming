#!/usr/bin/python3
"""
    Square class with size
"""


class Square(object):
    """
        A Square class to be instantiated with a size
    """

    def __init__(self, size):
        """
            Initializing class and constructing square with a size.

            Args:
                size(int): The size of the square to be constructed.
        """
        self.__size = size
