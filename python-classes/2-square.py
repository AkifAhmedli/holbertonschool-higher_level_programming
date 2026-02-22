#!/usr/bin/python3
"""Module for Square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Init square with size validation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
