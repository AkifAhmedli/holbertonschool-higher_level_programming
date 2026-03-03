#!/usr/bin/python3
"""
Filtrasiya imkanı olan Student klası.
"""


class Student:
    """
    Tələbə haqqında məlumatları saxlayan və JSON formatına hazırlayan klas.
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
        Student instansiyasının lüğət təsvirini qaytarır.
        Əgər attrs siyahıdırsa, yalnız orada göstərilən atributları qaytarır.
        """
        # Əgər attrs siyahı deyilsə və ya içindəki hər şey string deyilsə,
        # bütün atributları qaytar (əvvəlki tapşırıqdakı kimi)
        if not isinstance(attrs, list) or \
           not all(isinstance(i, str) for i in attrs):
            return self.__dict__

        # Əgər attrs düzgün siyahıdırsa, filtrasiya aparırıq
        filtered_dict = {}
        for key in attrs:
            if key in self.__dict__:
                filtered_dict[key] = self.__dict__[key]
        return filtered_dict
