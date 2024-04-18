#!/usr/bin/python3
"""Lists states"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306
        )
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id`")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == "N":
            print(row)
    cur.close()
    db.close()