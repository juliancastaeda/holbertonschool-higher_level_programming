#!/usr/bin/python3
#
import MySQLdb
db = "hbtn_0e_0_usa"
host = "localhost"
user = "root"
passwd = "root"
port = 3306
charset = "utf8"
conn = MySQLdb.connect(host, port, user, passwd, db, charset)
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
