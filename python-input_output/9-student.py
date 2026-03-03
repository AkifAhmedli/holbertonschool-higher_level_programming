#!/usr/bin/python3
"""
Tələbə (Student) klasını təyin edən modul.
"""


class Student:
    """
    Tələbə haqqında məlumatları saxlayan klas.
    """

    def __init__(self, first_name, last_name, age):
        """
        Yeni bir Student instansiyası yaradır.

        Args:
            first_name (str): Tələbənin adı.
            last_name (str): Tələbənin soyadı.
            age (int): Tələbənin yaşı.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Student instansiyasının lüğət (dict) təsvirini qaytarır.
        """
        return self.__dict__
