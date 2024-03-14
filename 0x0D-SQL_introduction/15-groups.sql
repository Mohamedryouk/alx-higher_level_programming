--lists the number of records with the same score in the table second_table.
USE hbtn_0c_0d_;

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
