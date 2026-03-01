#!/usr/bin/python3
"""BaseGeometry-dən miras alan Rectangle sinfini təyin edir."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """BaseGeometry əsasında düzbucaqlını təmsil edir."""

    def __init__(self, width, height):
        """Yeni bir Rectangle yaradır.

        Arqumentlər:
            width (int): Düzbucaqlının eni.
            height (int): Düzbucaqlının hündürlüyü.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Düzbucaqlının sahəsini qaytarır."""
        return self.__width * self.__height

    def __str__(self):
        """Rectangle-ın str() və print() təsvirini qaytarır."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
