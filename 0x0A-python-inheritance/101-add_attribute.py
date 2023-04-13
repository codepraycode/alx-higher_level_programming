#!/usr/bin/python3
"""Function to add attribute to an object if possible,
    otherwise throws exception.

    Prototype: def add_attribute(obj, key, value)
        Args:
            obj: object to add attribute to
            key(str): name of the attribute
            value(any): value to be associated with `key`

        Raises:
            TypeError: if the object can't have new attribute
                exception message could be `can't add new attribute`
"""


def add_attribute(obj, key, value):
    """Function to add attribute to an object if possible,
    otherwise throws exception.

    Args:
        obj: object to add attribute to
        key(str): name of the attribute
        value(any): value to be associated with `key`

    Raises:
        TypeError: if the object can't have new attribute
            exception message could be `can't add new attribute`
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    setattr(obj, key, value)
