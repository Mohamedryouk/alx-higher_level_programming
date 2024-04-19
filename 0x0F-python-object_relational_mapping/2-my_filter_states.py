#!/usr/bin/python3
import MySQLdb
import sys

def search_states(username, password, database, state_name):
    """Search for the states"""
    try:
        # Connect to MySQL server
        conn = MySQLdb.connect(host="localhost",
                               user=username,
                               passwd=password,
                               db=database,
                               port=3306)
        
        # Create cursor object
        cur = conn.cursor()

        # Create SQL query with user input
        query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY states.id ASC".format(state_name)

        # Execute the query
        cur.execute(query)

        # Fetch all the rows
        rows = cur.fetchall()

        # Display results
        for row in rows:
            print(row)

        cur.close()
        conn.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    search_states(username, password, database, state_name)
