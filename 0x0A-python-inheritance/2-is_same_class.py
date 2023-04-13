#!/usr/bin/python3
"""Function that returns True if the
    object is exactly an instance of the specified class; otherwise False.

    Prototype: def is_same_class(obj, a_class)
        Args:
            obj: object to check
            a_class: class used to check object
        Returns:
            bool: returns True if the object is exactly an instance
            of the `a_class`; otherwise False.
"""


def is_same_class(obj, a_class):
    """Function that returns True if the
    object is exactly an instance of the specified class; otherwise False.

    Args:
        obj: object to check
        a_class: class used to check object
    Returns:
        bool: returns True if the object is exactly an instance 
        of the `a_class`; otherwise False.
    """
    return type(obj) == a_class
