#!/usr/bin/python3

def uppercase(str):
    """Sətirdəki bütün kiçik hərfləri böyüyə çevirib çap edir."""
    for char in str:
        # Əgər simvol kiçik hərfdirsə (97-122 arası)
        if ord(char) >= 97 and ord(char) <= 122:
            # Onu böyük hərflə əvəz edirik (32 çıxmaqla)
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")  # Sonda yeni sətir
