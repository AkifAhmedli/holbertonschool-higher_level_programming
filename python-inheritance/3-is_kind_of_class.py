#!/usr/bin/python3
"""
Bu modul obyektin sinif və ya miras mənsubiyyətini yoxlayan funksiyanı ehtiva edir.
"""


def is_kind_of_class(obj, a_class):
    """Obyektin bir sinifdən və ya ondan miras alan sinifdən olmasını yoxlayır.

    Args:
        obj: Yoxlanılacaq obyekt.
        a_class: Müqayisə ediləcək sinif.

    Returns:
        bool: Əgər obyekt a_class-ın instansiyasıdırsa və ya a_class-dan
        miras alan bir sinfin instansiyasıdırsa True, əks halda False.
    """
    return isinstance(obj, a_class)
