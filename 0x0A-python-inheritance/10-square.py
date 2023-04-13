#!/usr/bin/python3
"""Square  class, a sub-class of Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """Square class, a sub-class of Rectangle class"""

    def __init__(self, size):
        """Initialize an instance with width and height

        Notes: `size` will be validated by `integer_validator`
            from `BaseGeometry`.

        Args:
            size(int): size of Square instance
        """

        BaseGeometry.integer_validator(self, 'size', size)
        self.__size = size

    def area(self):
        """Returns a calculated area of the instance"""
        return self.__size ** 2
