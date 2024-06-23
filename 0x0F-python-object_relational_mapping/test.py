#!/usr/bin/python3
import MySQLdb

conn = MySQLdb.connect(
    user='root',
    passwd='',
    db='hbtn_0e_0_usa'
)
c = conn.cursor()
c.execute('SELECT * FROM states')
rows = c.fetchall()
for row in rows:
    print(row)
