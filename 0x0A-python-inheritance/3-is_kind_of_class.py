#!/usr/bin/python3
"""Function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.

    Prototype: def is_kind_of_class(obj, a_class)
        Args:
            obj: object to check
            a_class: class used to check object
        Returns:
            bool: returns True if the object is an instance of,
                or if the object is an instance of a class that inherited from,
                the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Function that returns True if the
    object is exactly an instance of the specified class; otherwise False.

    Args:
        obj: object to check
        a_class: class used to check object
    Returns:
        bool: returns True if the object is an instance of,
            or if the object is an instance of a class that inherited from,
            the specified class ; otherwise False.
    """
    return isinstance(obj, a_class)
