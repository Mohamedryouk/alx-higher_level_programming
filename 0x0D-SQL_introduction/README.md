# Learning SQL - Task Files

This repository contains task files related to learning SQL. Each task file represents a specific SQL-related task that I have completed as part of my learning process.

## Overview

### Tasks

1. **0-list_databases.sql**: SQL script to list all databases on the MySQL server.
2. **1-create_database_if_missing.sql**: SQL script to create a database only if it doesn't already exist.
3. **2-remove_database.sql**: SQL script to remove a database from the MySQL server.
4. **3-list_tables.sql**: SQL script to list all tables in a specific database.
5. **4-first_table.sql**: SQL script to create a table in a database.
6. **5-full_table.sql**: SQL script to create a table with specific fields and properties.
7. **6-list_values.sql**: SQL script to list all records in a specific table.

### Usage

To use these task files, you'll need access to a MySQL server. Each task file contains SQL commands to perform specific actions related to database management and querying. 

For example, you can run the `0-list_databases.sql` script to list all databases on your MySQL server by using the following command:

```bash
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
