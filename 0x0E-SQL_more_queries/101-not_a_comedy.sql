-- Query to list shows not in comedy genre
SELECT DISTINCT title
  FROM tv_shows AS shows
	 LEFT JOIN tv_show_genres AS show_genres
	     ON show_genres.show_id = shows.id
	 LEFT JOIN tv_genres AS genres
	     ON genres.id = show_genres.genre_id
 WHERE shows.title NOT IN
       (SELECT title
	  FROM tv_shows AS shows
		 INNER JOIN tv_show_genres AS show_genres
		     ON shows.id = show_genres.show_id
		 INNER JOIN tv_genres AS genres
		     ON genres.id = show_genres.genre_id
	 WHERE genres.name = 'Comedy')
ORDER BY title;
