-- Uses th hbtn_0d_tvshows database to list all genres of the show Dexter

SELECT name
FROM tv_genres
LEFT JOIN tv_shows_genres ON tv_genres.id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
GROUP BY name
ORDER BY name ASC;
