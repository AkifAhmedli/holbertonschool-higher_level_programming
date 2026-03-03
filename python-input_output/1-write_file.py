#!/usr/bin/python3
"""
Bu modul fayla yazı yazmaq üçün funksiyanı ehtiva edir.
"""


def write_file(filename="", text=""):
    """
    Mətni UTF8 formatında fayla yazır və yazılan simvolların sayını qaytarır.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
