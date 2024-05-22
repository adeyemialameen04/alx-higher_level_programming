-- Subqueries.
SELECT id, name
FROM states
WHERE state_id = (SELECT id from states WHERE name = "California");
