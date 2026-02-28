#!/usr/bin/python3
"""BaseGeometry klasını təyin edən modul."""


class BaseGeometry:
    """Həndəsi fiqurlar üçün baza klası."""

    def area(self):
        """Sahəni hesablayan metod (hələ tətbiq olunmayıb).

        Raises:
            Exception: area() metodu tətbiq olunmadıqda atılır.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Daxil edilən dəyərin tam ədəd və müsbət olmasını yoxlayır.

        Args:
            name (str): Dəyişənin adı.
            value (int): Yoxlanılacaq dəyər.

        Raises:
            TypeError: value tam ədəd (int) deyilsə.
            ValueError: value 0-dan kiçik və ya bərabərdirsə.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
