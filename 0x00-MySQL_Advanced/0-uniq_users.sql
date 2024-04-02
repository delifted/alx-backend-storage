-- Creates table users
-- If the table already exists, this script will not fail
-- id column is an integer, never null, auto increment and primary key
-- email column is a string of maximum 255 characters, never null, and unique
-- name column is a string of maximum 255 characters
CREATE TABLE IF NOT EXISTS users (
  id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name VARCHAR(255)
);