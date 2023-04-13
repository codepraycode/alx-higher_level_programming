#!/usr/bin/python3
"""Function that creates an Object from a "JSON file"

    Prototype: def load_from_json_file(filename)
        Args:
            filename(str): file to load
"""
import json


def load_from_json_file(filename):
    """Function that creates an Object from a "JSON file"

    Args:
        filename(str): file to load
    """

    with open(filename, mode="r", encoding="utf-8") as file:
        _obj = file.read(filename)

        return json.loads(_obj)
