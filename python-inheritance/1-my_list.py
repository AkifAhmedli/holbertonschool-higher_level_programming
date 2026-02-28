#!/usr/bin/python3
"""
Bu modul list-dən miras alan MyList klasını təyin edir.
"""


class MyList(list):
    """list klasını genişləndirən xüsusi klas."""

    def print_sorted(self):
        """Siyahıdakı elementləri artan sıra ilə çap edir.

        Orijinal siyahının sırasını dəyişmir.
        """
        print(sorted(self))
