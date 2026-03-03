#!/usr/bin/python3
"""
Bu modul mətni faylın sonuna əlavə edən funksiyanı ehtiva edir.
"""


def append_write(filename="", text=""):
    """
    UTF8 formatında mətni faylın sonuna əlavə edir və
    əlavə olunan simvolların sayını qaytarır.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
