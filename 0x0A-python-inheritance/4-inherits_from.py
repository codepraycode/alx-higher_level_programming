#!/usr/bin/python3
"""Function that returns True if the object is an instance of a
    class that inherited (directly or indirectly) from the specified class;
    otherwise False.

    Prototype: def inherits_from(obj, a_class)
        Args:
            obj: object to check
            a_class: class used to check object
        Returns:
            bool: True if the object is an instance of a
                class that inherited (directly or indirectly) from the specified class;
                otherwise False.
"""


def inherits_from(obj, a_class):
    """Function that returns True if the object is an instance of a
    class that inherited (directly or indirectly) from the specified class;
    otherwise False.

    Args:
        obj: object to check
        a_class: class used to check object
    Returns:
        bool: True if the object is an instance of a
            class that inherited (directly or indirectly) from the specified class;
            otherwise False.
    """
    return False if type(obj) == a_class else isinstance(obj, a_class)
