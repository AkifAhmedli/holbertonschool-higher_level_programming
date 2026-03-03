#!/usr/bin/python3
"""
Bu modul faylı oxumaq (və ya yazmaq) funksiyasını ehtiva edir.
Bu sətir modulun __doc__ atributunu təmin edir.
"""


def read_file(filename=""):
    """Faylı UTF8 olaraq oxuyur və çap edir."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
