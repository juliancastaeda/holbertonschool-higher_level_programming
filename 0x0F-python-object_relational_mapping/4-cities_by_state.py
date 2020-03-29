#!/usr/bin/python3
"""


"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv):
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
    connection = MySQLdb.connect(host='localhost',
                         user=username, passwd=password, db=database)
    cur = connection.cursor()
    cur.execute('''SELECT cities.id, cities.name,
                states.name FROM cities INNER JOIN
                states ON cities.state_id = states.id''')
    for row in cur.fetchall():
        print(row)
    cur.close()
    connection.close()
