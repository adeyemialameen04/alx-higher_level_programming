#!/usr/bin/python3
"""5"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    username, password, db, state_name = argv[1], argv[2], argv[3], argv[4]
    conn = MySQLdb.connect(user=username, passwd=password, db=db)
    c = conn.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    c.execute(query, (state_name,))
    rows = c.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    c.close()
    conn.close()
