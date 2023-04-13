#!/usr/bin/python3
"""Function that appends a string at the end of a text file (UTF8)
and returns the number of characters added

    Prototype: def append_write(filename="", text="")
        Args:
            filename(str): file name to read
            text(str): a string parameter
"""


def append_write(filename="", text=""):
    """Function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename(str): file name to read
        text(str): a string parameter
    """

    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)

    return len(text)
