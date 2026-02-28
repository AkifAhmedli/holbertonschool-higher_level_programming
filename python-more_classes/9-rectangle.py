#!/usr/bin/python3
"""
Bu modul Rectangle klasını təyin edir.
"""


class Rectangle:
    """Düzbucaqlını təmsil edən klas."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Yeni bir Rectangle yaradır və sayğacı artırır."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Eni geri qaytarır."""
        return self.__width

    @width.setter
    def width(self, value):
        """Eni təyin edir (validasiya ilə)."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Hündürlüyü geri qaytarır."""
        return self.__height

    @height.setter
    def height(self, value):
        """Hündürlüyü təyin edir (validasiya ilə)."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Düzbucaqlının sahəsini qaytarır."""
        return self.__width * self.__height

    def perimeter(self):
        """Düzbucaqlının perimetrini qaytarır."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Düzbucaqlını print_symbol ilə vizual təsvir edir."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_lines = []
        for i in range(self.__height):
            rect_lines.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect_lines)

    def __repr__(self):
        """Obyektin rəsmi simvolik təsvirini qaytarır."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Obyekt silindikdə mesaj çap edir və sayğacı azaldır."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """İki düzbucaqlıdan sahəsi böyük olanı qaytarır."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Yeni bir kvadrat (eni = hündürlüyü = size) instansiyası qaytarır."""
        return cls(size, size)
