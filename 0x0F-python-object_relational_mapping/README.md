# README for MySQL

This directory contains examples for using MySQL with Python.

## Getting Started

To use MySQL in Python, you need to:

1. Install the `mysql-connector-python` package:


pip install mysql-connector-python
 

2. Import the `mysql.connector` module:


import mysql.connector


3. Connect to the MySQL database by creating a `MySQLConnection` object:


mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)


4. Get a cursor to execute queries:

 
mycursor = mydb.cursor()


5. Execute SQL queries using the cursor:


mycursor.execute("SELECT * FROM customers")
 

6. Fetch results:


result = mycursor.fetchall() 


7. Commit changes:


mydb.commit()


8. Close the connection:


mydb.close()


See the examples in this directory for more details on connecting to MySQL and querying data in Python.

