#!/usr/bin/python3
"""Function that writes a string to a text file (UTF8) and
returns the number of characters written

    Prototype: def write_file(filename="", text="")
        Args:
            filename(str): file name to read
            text(str): a string parameter
"""


def write_file(filename="", text=""):
    """Function that writes a string to a text file (UTF8) and
    returns the number of characters written

    Args:
        filename(str): file name to read
        text(str): a string parameter
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)

    return len(text)
