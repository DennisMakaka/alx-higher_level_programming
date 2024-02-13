-- Script to list all records of the second_table in the hbtn_0c_0 database
-- Results display both the score and the name, ordered by score (top first)
-- Execute this script with the database name as an argument to the mysql command

SELECT `score`, `name`
FROM `second_table`
ORDER BY `score` DESC;
