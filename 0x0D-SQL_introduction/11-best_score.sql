-- Script to list all records with a score >= 10 in the second_table of the hbtn_0c_0 database
-- Results display both the score and the name, ordered by score (top first)
-- Execute this script with the database name as an argument to the mysql command

SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
