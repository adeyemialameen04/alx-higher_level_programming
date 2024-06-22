#!/usr/bin/python3
"""1"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db = argv[3]

    conn = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=db,
        port=3306
    )
    c = conn.cursor()
    c.execute("SELLECT * FROM state WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    conn.close()
