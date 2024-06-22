#!/usr/bin/python3
"""0"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db = argv[3]

    conn = MySQLdb.connect(
        user=username,
        passwd=password,
        db=db
    )
    c = conn.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    conn.close()
