#!/usr/bin/python3
"""Rectangle class, a sub-class of BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class, a sub-class of BaseGeometry class"""

    def __init__(self, width, height):
        """Initialize an instance with width and height

        Notes: `width` and `height` will be validated by `integer_validator`
            from `BaseGeometry`.

        Args:
            width(int): Width of rectangle instance
            height(int): Height of rectangle instance
        """

        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width

        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height

    def area(self):
        """Returns a calculated area of the instance"""
        return self.__width * self.__height

    def print(self):
        """Returns a string representation of the instance
        like [Rectangle] <width>/<height>
        """
        print(self)
    
    def __str__(self):
        """Returns a printable representation of the instance"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
