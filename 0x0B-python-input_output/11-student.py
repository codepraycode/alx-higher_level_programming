#!/usr/bin/python3
"""Student class"""


class Student(object):
    """Student class defined by `first_name` and
    `last_name` and `age`
    """

    def __init__(self, first_name, last_name, age):
        """Initialise Student instance

        Args:
            first_name(str): First name of instance
            last_name(str): Last name of instance
            age(int): age of instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a dictionary representation of instance

        Args:
            attrs(list): [optional] A list of strings of items to be retrieved

        Returns:
            dict: __dict__ property of instnace
        """

        if attrs is None:
            return self.__dict__

        _res = {}

        for each in attrs:
            val = self.__dict__.get(each)
            if val is not None:
                _res[each] = val

        return _res

    def reload_from_json(self, json):
        """Method that replaces all attributes of the Student instance

        Args:
            json(dict): a dictionary that contains data to work with.
        """

        for key, value in json.items():

            if self.__dict__.get(key) == self.first_name:
                self.first_name = value

            if self.__dict__.get(key) == self.last_name:
                self.last_name = value

            if self.__dict__.get(key) == self.age:
                self.age = value
