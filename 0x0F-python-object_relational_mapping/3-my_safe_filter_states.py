#!/usr/bin/python3
"""3"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db = argv[3]
    state_name = argv[4]

    conn = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=db,
        port=3306
    )
    c = conn.cursor()
    query = """
        SELECT *
        FROM states
        WHERE name = %s
        ORDER BY id ASC
    """
    c.execute(query, (state_name))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    conn.close()
