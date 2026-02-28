#!/usr/bin/python3
"""
Bu modul obyektin miras mənsubiyyətini yoxlayan funksiyanı ehtiva edir.
"""


def inherits_from(obj, a_class):
    """Obyektin bir sinifdən (birbaşa və ya dolayısı ilə) miras alıb-almadığını
    yoxlayır.

    Args:
        obj: Yoxlanılacaq obyekt.
        a_class: Müqayisə ediləcək sinif.

    Returns:
        bool: Əgər obyekt a_class-dan miras alan bir sinfin instansiyasıdırsa
        və özü birbaşa a_class deyilsə True, əks halda False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
