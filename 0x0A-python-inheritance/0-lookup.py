#!/usr/bin/python3
"""Function to get a list of all available attributes and methods
    of an object

    Prototype: def lookup(obj)
        Args:
            obj: object to lookup
        Returns:
            list: a list of available attributes and methods
"""


def lookup(obj):
    """A function that returns a list of available attributes
    and methods of an object

    Args:
        obj: an object instance of a class

    Returns:
        list: a list of available attributes and methods of `obj`
    """
    return dir(obj)
