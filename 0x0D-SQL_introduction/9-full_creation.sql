-- creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
USE hbtn_0c_0

CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(255), score INT);

INSERT INTO second_table (id, name, score) VALUES (1, John, 10);
INSERT INTO second_table (id, name, score) VALUES (2, Alex, 9);
INSERT INTO second_table (id, name, score) VALUES (3, Bob, 14);
INSERT INTO second_table (id, name, score) VALUES (4, George, 8);
