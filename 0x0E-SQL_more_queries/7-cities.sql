-- Cities.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
	FOREIGN KEY (state_id) REFERENCES states(id),
	name varchar(256) NOT NULL
);
