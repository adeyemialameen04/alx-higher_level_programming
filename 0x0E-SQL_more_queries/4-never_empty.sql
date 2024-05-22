-- Never empty.
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT NOT NULL DEFAULT 1,
	name varchar(256)
);
