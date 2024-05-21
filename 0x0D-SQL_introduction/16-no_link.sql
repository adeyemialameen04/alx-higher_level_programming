-- Say my name.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
Order BY score DESC;
