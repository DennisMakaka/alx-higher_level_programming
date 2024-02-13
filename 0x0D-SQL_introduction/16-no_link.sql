-- Script to list all records of the second_table in the hbtn_0c_0 database
-- Excludes rows without a name value
-- Results display the score and the name, sorted by descending score
-- Execute this script with the database name as an argument to the mysql command

SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
