#!/usr/bin/python3
"""
Tam seriyallaşdırma imkanı olan Student klası.
"""


class Student:
    """
    Tələbə haqqında məlumatları idarə edən klas.
    """

    def __init__(self, first_name, last_name, age):
        """
        Yeni bir Student instansiyası yaradır.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Obyekti lüğətə (dict) çevirir.
        Əgər attrs siyahıdırsa, yalnız siyahıdakı atributları seçir.
        """
        if isinstance(attrs, list) and \
           all(isinstance(i, str) for i in attrs):
            res = {}
            for k in attrs:
                if k in self.__dict__:
                    res[k] = self.__dict__[k]
            return res
        return self.__dict__

    def reload_from_json(self, json):
        """
        Obyektin atributlarını JSON lüğəti ilə əvəzləyir.

        Args:
            json (dict): Açar-dəyər cütlüyü olan lüğət.
        """
        for key, value in json.items():
            setattr(self, key, value)
