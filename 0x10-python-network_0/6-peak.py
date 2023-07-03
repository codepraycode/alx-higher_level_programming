#!/usr/bin/python3
"""Algorithms for list of integers."""


def find_peak(list_of_integers):
    """Function to finds a peak in a list of unsorted integers.

    Args:
        list_of_integers: [int] - A list fof intergers.
    """
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
