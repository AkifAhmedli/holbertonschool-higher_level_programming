#!/usr/bin/python3
"""
Obyektin JSON seriyallaşdırılması üçün lüğət təsvirini qaytaran funksiya.
"""


def class_to_json(obj):
    """
    Obyektin bütün atributlarını lüğət (dict) formatında qaytarır.
    """
    return obj.__dict__
