-- Create database 
DROP DATABASE IF EXISTS hbtn_0c_0;
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
USE hbtn_0c_0;

-- Create table
CREATE TABLE IF NOT EXISTS first_table (
    id INT, 
    name VARCHAR(256),
    score INT
);

-- Display first_table description
SHOW CREATE TABLE first_table;

-- Convert database and table to UTF8
ALTER DATABASE hbtn_0c_0
    CHARACTER SET = utf8mb4
    COLLATE = utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.first_table
    CONVERT TO CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.first_table
    MODIFY name VARCHAR(256)
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;
