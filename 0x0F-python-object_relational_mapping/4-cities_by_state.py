#!/usr/bin/python3
"""4"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    username, password, db = argv[1], argv[2], argv[3]
    conn = MySQLdb.connect(user=username, passwd=password, db=db)
    c = conn.cursor()

    query = """
    SELECT cities.id, cities.name, states.name
    FROM CITIES
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    c.execute(query)

    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    conn.close()
