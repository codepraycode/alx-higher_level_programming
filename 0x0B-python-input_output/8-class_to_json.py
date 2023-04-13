#!/usr/bin/python3
"""Function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer and boolean) for
    JSON serialization of an object

    Prototype: def class_to_json(obj)
        Args:
            obj(any): an instance
"""


def class_to_json(obj):
    """Function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer and boolean) for
    JSON serialization of an object

    Args:
        obj(any): an instance

    Returns:
        dict: object __dict__
    """

    return obj.__dict__
