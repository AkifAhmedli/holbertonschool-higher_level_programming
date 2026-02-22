#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The module contains one function: add_integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    a and b must be integers or floats, otherwise raise a TypeError.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
