#!/usr/bin/python3
"""


"""
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    stateNameSearched = sys.argv[4]
    connection = MySQLdb.Connect(host="localhost",
                                 port=3306,
                                 user=username,
                                 passwd=password,
                                 db=dbname,
                                 charset="utf8")
    cur = connection.cursor()
    cur.execute('''
                SELECT * FROM states
                WHERE states.name = '{}' ORDER BY id ASC
                '''.format(stateNameSearched))
    row = cur.fetchall()
    for row in row:
        print(row)
