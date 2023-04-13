#!/usr/bin/python3
"""Function that reads a text file (UTF8) and prints it to stdout

    Prototype: def read_file(filename="")
        Args:
            filename: file name to read
"""


def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename: file name to read
    """

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
