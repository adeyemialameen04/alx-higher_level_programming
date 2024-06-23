#!/usr/bin/python3
""" safely List all states that start with 'N' """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    conn = argv[3]
    state_name = argv[4]

    conn = MySQLdb.connect(user=username, passwd=password, db=conn)
    c = conn.cursor()
    query = """
        SELECT *
        FROM states
        WHERE name = %s
        ORDER BY id ASC
        """
    c.execute(query, (state_name, ))

    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    conn.close()
