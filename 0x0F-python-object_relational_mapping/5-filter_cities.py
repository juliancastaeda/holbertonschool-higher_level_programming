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
        state = sys.argv[4]
    connection = MySQLdb.connect(host='localhost', port=3306, user=username,
                         passwd=password, db=database, charset="utf8")
    cur = connection.cursor()
    cur.execute('''SELECT name FROM cities WHERE state_id=(SELECT
                    id FROM states WHERE name='{}')'''.format(state))
    city = ""
    for i in cur.fetchall():
        name_city = city + i[0] + ", "
    print(city[0:-2])
    cur.close()
    connection.close()
