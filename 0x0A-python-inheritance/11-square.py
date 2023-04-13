#!/usr/bin/python3
"""Square  class, a sub-class of Rectangle class"""


PrevSquareClass = __import__('10-square').Square


class Square(PrevSquareClass):
    """Square class, a sub-class of Rectangle class"""

    def __init__(self, size):
        """Initialize an instance with width and height

        Notes: `size` will be validated by `integer_validator`
            from `BaseGeometry`.

        Args:
            size(int): size of Square instance
        """
        super().__init__(size)

    def area(self):
        """Returns a calculated area of the instance"""
        return self.__size ** 2

    def __str__(self):
        """Returns a prinatable representation of the instance
        like [Square] <width>/<height>
        """
        return "[Square] {0:d}/{0:d}".format(self.__size)
