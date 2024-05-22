-- Not my genre.
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (
  SELECT tv_show_genres.genre_id
  FROM tv_shows
  JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
  WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name ASC;
