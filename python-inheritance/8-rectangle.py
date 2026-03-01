#!/usr/bin/python3
"""BaseGeometry-dən miras alan Rectangle (Düzbucaqlı) sinfini təyin edir."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry əsasında düzbucaqlını təmsil edir."""

    def __init__(self, width, height):
        """Yeni bir Rectangle (Düzbucaqlı) yaradır.

        Arqumentlər:
            width (int): Düzbucaqlının eni.
            height (int): Düzbucaqlının hündürlüyü.
        """
        # Eni validator vasitəsilə yoxlayırıq
        self.integer_validator("width", width)
        self.__width = width

        # Hündürlüyü validator vasitəsilə yoxlayırıq
        self.integer_validator("height", height)
        self.__height = height
