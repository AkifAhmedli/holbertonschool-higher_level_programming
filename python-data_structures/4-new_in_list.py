#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Orijinal siyahının kopyasını yaradırıq
    copy_list = my_list[:]

    # İndeksi yoxlayırıq
    if idx < 0 or idx >= len(my_list):
        return copy_list

    # Kopyalanmış siyahıda elementi dəyişirik
    copy_list[idx] = element
    return copy_list
