#!/usr/bin/python3
"""Function that writes an Object to a text file, using a JSON representation

    Prototype: def save_to_json_file(my_obj, filename)
        Args:
            my_obj(dict): a dictionary object
            filename(str): file directory to write object to
"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file, using a JSON representation

    Args:
        my_obj(dict): a dictionary object
        filename(str): file directory to write object to
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        _obj = json.dumps(my_str)
        file.write(_obj)
