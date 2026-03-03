#!/usr/bin/python3
"""
Paskal üçbucağı generatoru.
"""


def pascal_triangle(n):
    """
    n ölçülü Paskal üçbucağını siyahılar siyahısı kimi qaytarır.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        # Hər yeni sətir həmişə 1 ilə başlayır
        row = [1]

        # Əvvəlki sətri götürürük
        prev_row = triangle[i - 1]

        # Aradakı rəqəmləri hesablayırıq:
        # Hər bir element prev_row[j-1] + prev_row[j] cəmidir
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        # Hər yeni sətir həmişə 1 ilə bitir
        row.append(1)

        # Sətri üçbucağa əlavə edirik
        triangle.append(row)

    return triangle
