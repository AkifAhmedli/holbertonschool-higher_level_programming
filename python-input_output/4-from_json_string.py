#!/usr/bin/python3
"""
Bu modul JSON sətrini Python obyektinə çevirən funksiyanı ehtiva edir.
"""
import json


def from_json_string(my_str):
    """
    JSON formatında olan mətni (string) Python məlumat strukturuna
    (məsələn: list, dict) çevirir və qaytarır.
    """
    return json.loads(my_str)
