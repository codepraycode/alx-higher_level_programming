#!/usr/bin/python3
"""Rectangle class, a sub-class of BaseGeometry class"""
import BaseGeometry from 7-base_geometry


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

        self.integer_validator('width', width)
        self.__width = width

        self.integer_validator('height', height)
        self.__height = height
