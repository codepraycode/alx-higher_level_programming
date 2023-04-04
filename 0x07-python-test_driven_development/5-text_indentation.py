#!/usr/bin/python3
"""Function that prints a text with 2 new lines after each of these characters: ., ? and :
    Prototye: def text_indentation(text)

        Args:
            text(str): Text argument

        Raises:
            TypeError: if text is not a string
                expected message should be: `text must be a string`
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of special characters
        Special characters includes: `.`, `?` and `:`

    Args:
        text(str): Text argument

    Raises:
        TypeError: if text is not a string
            expected message should be: `text must be a string`
    """
    _special_char = ['.', '?', ':']

    # TypeErrors
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for tx in text:
        print(tx, end="")
        if tx in _special_char:
            print('\n\n', end="")
