-- Query for hbtn_0d_tvshows db listing all ID including NULL
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows AS tv_shows
	 LEFT JOIN tv_show_genres AS tv_show_genres
	    ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
