#!/usr/bin/python3
"""
İstifadəçinin daxil etdiyi ştat adına görə filtrləmə aparan skript.
SQL injection-dan qorunmaq üçün parametrli sorğudan istifadə olunur.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Verilənlər bazasına qoşulma
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()

    # İstifadəçinin axtardığı ştat adı (4-cü arqument)
    state_name_searched = sys.argv[4]

    # SQL Injection-dan qorunmaq üçün %s formatından istifadə edirik.
    # Diqqət: '%s' dırnaq içində yazılmır, MySQLdb bunu özü həll edir.
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    # İkinci arqument mütləq tuple (nəticə, ) şəklində olmalıdır
    cursor.execute(query, (state_name_searched,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
