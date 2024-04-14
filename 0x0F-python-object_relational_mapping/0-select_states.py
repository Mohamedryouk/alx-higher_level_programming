#!/usr/bin/python3
import MySQLdb
import sys
def list_states(username, password, database):
    try:
        db = MySQLdb.connect(host="localhost", port=8080, user=username, passwd=password, db=database)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states")
        results = cursor.fetchall()
        for row in results:
            print(row)
        
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
if __name__ == "__name__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)
