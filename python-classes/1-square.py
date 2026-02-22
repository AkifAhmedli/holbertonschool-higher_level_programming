#!/usr/bin/python3
"""Square klasını təyin edən modul."""


class Square:
    """Kvadratı təmsil edən klas."""

    def __init__(self, size):
        """Yeni bir Square nümunəsi yaradır.

        Args:
            size: Kvadratın tərəfinin ölçüsü.
        """
        self.__size = size
