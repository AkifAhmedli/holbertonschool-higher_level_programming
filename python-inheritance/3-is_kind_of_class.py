#!/usr/bin/python3
"""
Bu modul obyektin sinif mənsubiyyətini yoxlayan funksiyanı ehtiva edir.
"""


def is_same_class(obj, a_class):
    """Obyektin dəqiq göstərilən sinfin instansiyası olub-olmadığını yoxlayır.

    Args:
        obj: Yoxlanılacaq obyekt.
        a_class: Müqayisə ediləcək sinif.

    Returns:
        bool: Əgər obyekt dəqiq a_class sinfindəndirsə True, əks halda False.
    """
    return type(obj) is a_class
