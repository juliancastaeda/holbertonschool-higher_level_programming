#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3],
    state=sys.argvargv[4]
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=username,
                           passwd=password,
                           db=dbname,
    cur = conn.cursor()
    cur.execute('''
                SELECT * FROM states
                WHERE states.name = '{}' ORDER BY id ASC
                '''.format(state))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
