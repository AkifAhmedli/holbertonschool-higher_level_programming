#!/usr/bin/python3
"""
Bu modul BaseGeometry klasını təyin edir.
"""


class BaseGeometry:
    """Həndəsi fiqurlar üçün baza klası."""

    def area(self):
        """Sahəni hesablayan metod.

        Raises:
            Exception: area() is not implemented mesajı ilə.
        """
        raise Exception("area() is not implemented")
