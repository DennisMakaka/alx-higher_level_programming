-- Script to list the number of records with the same score in the second_table of the hbtn_0c_0 database
-- Results display the score and the number of records for each score
-- Sorted by the number of records (descending)
-- Execute this script with the database name as an argument to the mysql command

SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
