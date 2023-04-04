#!/usr/bin/python3
"""Function that prints My name is <first name> <last name>
    Prototye: def say_my_name(first_name, last_name="")

        Args:
            first_name (str): First name argument
            last_name (str, optional): Second name argument

        Raises:
            TypeError: There are differenct cases
                case1: if first_name is not a string
                    expected message should be:
                    `first_name must be a string`
                case2: if last_name is not a string
                    expected message should be:
                    `last_name must be a string`
"""


def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>
        from parameters `first_name` `last_name`

    Args:
            first_name (str): First name argument
            last_name (str, optional): Second name argument

        Raises:
            TypeError: There are differenct cases
                case1: if first_name is not a string
                    expected message should be:
                    `first_name must be a string`
                case2: if last_name is not a string
                    expected message should be:
                    `last_name must be a string`
    """
    # TypeErrors
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
