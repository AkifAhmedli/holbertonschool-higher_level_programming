#!/usr/bin/python3

def print_last_digit(number):
    """Ədədin sonuncu rəqəmini çap edir və qaytarır."""
    # Ədədin mütləq qiymətinin 10-a bölünməsindən qalan qalığı tapırıq
    last_digit = abs(number) % 10
    
    # Sonuncu rəqəmi yeni sətir olmadan çap edirik
    print("{}".format(last_digit), end="")
    
    # Tapdığımız rəqəmi geri qaytarırıq (Return)
    return last_digit
