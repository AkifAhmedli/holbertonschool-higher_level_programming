#!/usr/bin/python3
"""
'hbtn_0e_0_usa' bazasından adı 'N' ilə başlayan ştatları siyahılayır.
MySQLdb modulundan istifadə olunur.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Arqumentlərin götürülməsi
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Serverə qoşulma
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    cursor = db.cursor()

    # SQL sorğusu: 'N' ilə başlayanları seçir və ID-yə görə sıralayır.
    # BINARY istifadə etmək böyük 'N' olduğunu dəqiqləşdirir.
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Nəticələrin emalı
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Bağlantıların bağlanması
    cursor.close()
    db.close()
