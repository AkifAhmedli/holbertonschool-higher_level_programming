#!/usr/bin/python3
"""
Bu modul eni və hündürlüyü olan Rectangle klasını təyin edir.
"""


class Rectangle:
    """Düzbucaqlını təmsil edən klas."""

    def __init__(self, width=0, height=0):
        """Yeni bir Rectangle yaradır.

        Args:
            width (int): Düzbucaqlının eni.
            height (int): Düzbucaqlının hündürlüyü.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Eni geri qaytarmaq üçün property (getter)."""
        return self.__width

    @width.setter
    def width(self, value):
        """Eni təyin etmək üçün setter (validasiya ilə)."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Hündürlüyü geri qaytarmaq üçün property (getter)."""
        return self.__height

    @height.setter
    def height(self, value):
        """Hündürlüyü təyin etmək üçün setter (validasiya ilə)."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
