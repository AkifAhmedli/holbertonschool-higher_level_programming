#!/usr/bin/python3
"""
Bu modul JSON faylından obyekt yaradan funksiyanı ehtiva edir.
"""
import json


def load_from_json_file(filename):
    """
    JSON formatlı faylı oxuyur və müvafiq Python obyektini qaytarır.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
