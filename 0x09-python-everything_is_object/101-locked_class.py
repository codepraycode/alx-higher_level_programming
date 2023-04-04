#!/usr/bin/python3

"""Defines a locked class `LockedClass`
    with no class or object attribute, that prevents the user from 
    dynamically creating new instance attributes, except if the new 
    instance attribute is called `first_name`.
"""


class LockedClass:
    """LockedClass with one attribute 'first_name'

        Prevent the new instance of LockedClass attributes
            for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]