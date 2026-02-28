#!/usr/bin/python3
"""
Bu modul obyektin sinif mənsubiyyətini yoxlayan funksiyanı ehtiva edir.
"""


def is_kind_of_class(obj, a_class):
    """Obyektin sinif və ya miras mənsubiyyətini yoxlayır.

    Args:
        obj: Yoxlanılacaq obyekt.
        a_class: Müqayisə ediləcək sinif.

    Returns:
        bool: a_class instansiyası və ya ondan miras alıbsa True.
    """
    return isinstance(obj, a_class)
