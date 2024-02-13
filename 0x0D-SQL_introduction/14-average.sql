-- Script to compute the score average of all records in the second_table of the hbtn_0c_0 database
-- Execute this script with the database name as an argument to the mysql command

SELECT AVG(`score`) AS `average`
FROM `second_table`;
