#!/usr/bin/python3
"""Function that inserts a line of text to a file,
after each line containing a specific string"

    Prototype: def append_after(filename="", search_string="", new_string="")
        Args:
            filename(str): file to load
            search_string(str): string parameter
            new_string(str): string parameter
"""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts a line of text to a file,
    after each line containing a specific string"

    Args:
        filename(str): file to load
        search_string(str): string parameter
        new_string(str): string parameter
    """

    with open(filename, mode="r+", encoding="utf-8") as file:
        content = file.readlines()
        new_content = ""

        for each_line in content:
            new_content += each_line

            if search_string in each_line:
                new_content += new_string

        # Go to the beginning of the file
        file.seek(0)
        file.write(new_content)  # write content.
