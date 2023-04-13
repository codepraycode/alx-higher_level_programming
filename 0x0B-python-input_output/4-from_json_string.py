#!/usr/bin/python3
"""Function 4-from_json_string.py

    Prototype: def from_json_string(my_str)
        Args:
            my_str(str): json object string
"""
import json


def from_json_string(my_str):
    """Function 4-from_json_string.py

    Args:
        my_str(str): json object string
    """

    return json.loads(my_str)
