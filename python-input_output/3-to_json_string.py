#!/usr/bin/python3
"""
Bu modul obyekti JSON sətrinə çevirən funksiyanı ehtiva edir.
"""
import json


def to_json_string(my_obj):
    """
    Obyektin (string) JSON təmsilini qaytarır.
    """
    return json.dumps(my_obj)
