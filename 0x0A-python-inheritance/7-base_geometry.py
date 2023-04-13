#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry(object):
    """BaseGeometry class"""

    def area(self):
        """A method to define the area of the geometry instance"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validates `value` parameter

        Args:
            name(str): a parameter
            value(int): a parameter

        Raises:
            TypeError: if `value` is not an integer.
                exception message could be `<name> must be an integer`
            ValueError: if `value` is less than or equal to 0.
                exception message could be `<name> must be greater than 0`
        """
        # Check for TypeError
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        # Check for ValueError
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
