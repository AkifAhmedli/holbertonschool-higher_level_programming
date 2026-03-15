#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument. Safe from SQL injections.
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

    # Sorğuda parametrli üsuldan (%s) istifadə edirik.
    # Bu, Check 9-da yoxlanılan xüsusi simvolların (məsələn: Arizona') 
    # təhlükəsiz şəkildə emal olunmasını təmin edir.
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    # execute funksiyasına arqumenti mütləq tuple daxilində göndər
    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Bağlantıları təmiz bağla
    cursor.close()
    db.close()
