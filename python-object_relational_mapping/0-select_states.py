#!/usr/bin/env python3
"""
hbtn_0e_0_usa verilənlər bazasından bütün ştatları siyahılayan skript.
Bu skript 3 arqument qəbul edir: mysql istifadəçi adı, şifrə və baza adı.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Komanda sətrindən arqumentlərin oxunması
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Verilənlər bazasına qoşulma
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    # Kursor obyektinin yaradılması (sorğuları icra etmək üçün)
    cursor = db.cursor()

    # SQL sorğusunun icrası
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Bütün nəticələrin götürülməsi
    rows = cursor.fetchall()

    # Nəticələrin nümunədəki kimi çap edilməsi
    for row in rows:
        print(row)

    # Bağlantıların bağlanması
    cursor.close()
    db.close()
