#!/usr/bin/python3
"""Function that returns the JSON representation of an object (string)

    Prototype: def to_json_string(my_obj):
        Args:
            my_obj(str): object string
"""
import json


def to_json_string(my_obj):
    """Function that returns the JSON representation of an object (string)

    Args:
        my_obj(str): object string
    """

    return json.dumps(my_obj)
