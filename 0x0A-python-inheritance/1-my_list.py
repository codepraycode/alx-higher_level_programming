#!/usr/bin/python3
"""MyList class (subclass of list)"""


class MyList(list):
    """MyList that inherit from `list` class with
    extra functionalities.
    """

    def print_sorted(self):
        """Method to display sorted list instance
        """
        print(sorted(self))
