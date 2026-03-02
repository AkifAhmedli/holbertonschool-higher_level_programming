#!/usr/bin/python3

def read_file(filename=""):
    """UTF8 formatlı mətni oxuyur və stdout-a çap edir."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
