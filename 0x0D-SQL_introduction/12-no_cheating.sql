-- Script to update the score of Bob to 10 in the second_table
-- Execute this script with the database name as an argument to the mysql command

UPDATE `second_table`
SET `score` = 10
WHERE `name` = "Bob";
