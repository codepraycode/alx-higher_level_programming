#!/usr/bin/python3
"""Magic Class"""
import math


class MagicClass(object):
    """Magic Class definition"""

    def __init__(self, radius=0):
        """Initializes MagicClass instance with given radius

        Args:
            radius(int optional): parameter for instance initialization
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate area

        Returns:
            float: calculated area with pi
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculate Circumference
        Returns:
            flaot: calculated circumference
        """
        return (2 * math.pi * self.__radius)