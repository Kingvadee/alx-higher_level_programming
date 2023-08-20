-- Query to list genres not linked to Dexter show
SELECT DISTINCT name
  FROM tv_genres AS genres
	 INNER JOIN tv_show_genres AS show_genres
	     ON genres.id = show_genres.genre_id
	 INNER JOIN tv_shows AS shows
	     ON show_genres.show_id = shows.id
 WHERE genres.name NOT IN
       (SELECT name
	  FROM tv_genres AS genres
		 INNER JOIN tv_show_genres AS show_genres
		     ON genres.id = show_genres.genre_id
		 INNER JOIN tv_shows AS shows
		     ON show_genres.show_id = shows.id
	 WHERE shows.title = 'Dexter')
ORDER BY genres.name;
