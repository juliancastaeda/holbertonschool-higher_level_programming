#!/usr/bin/python3
"""


"""
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state = sys.argv[4]
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
                '''.format(state))
    qR = cur.fetchall()
    for row in qR:
        print(row)
