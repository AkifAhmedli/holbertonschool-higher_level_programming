#!/usr/bin/python3
"""
Bu modul həndəsi fiqurlar üçün BaseGeometry klasını təyin edir.
"""


class BaseGeometry:
    """Həndəsi fiqurlar üçün baza klası."""

    def area(self):
        """Sahəni hesablayan metod (hələ tətbiq olunmayıb).

        Raises:
            Exception: area() is not implemented mesajı ilə.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Daxil edilən dəyərin müsbət tam ədəd olub-olmadığını yoxlayır.

        Args:
            name (str): Dəyişənin adı (həmişə string olduğu fərz edilir).
            value (int): Yoxlanılacaq dəyər.

        Raises:
            TypeError: Əgər value tam ədəd (int) deyilsə.
            ValueError: Əgər value 0-dan kiçik və ya bərabərdirsə.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
