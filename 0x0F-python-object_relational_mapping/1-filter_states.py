#!/usr/bin/python3
"""lists all states with a name starting with N"""
import MySQLdb
import sys

fi = 34


def list_states_with_n(username, password, database):
    """listing states"""
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password,
                             db=database)
        cursor = db.cursor()

        cursor.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        results = cursor.fetchall()
        for row in results:
            print(row)

        db.close()
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)
