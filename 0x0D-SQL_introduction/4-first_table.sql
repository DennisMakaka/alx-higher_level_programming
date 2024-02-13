-- Script to create the first_table if it doesn't exist in the current database
-- Execute this script with the database name as an argument to the mysql command

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
