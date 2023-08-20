-- Query to list shows by ranking
SELECT title, SUM(rate) AS rating
  FROM tv_shows AS shows
       INNER JOIN tv_show_ratings AS ratings
	   ON shows.id = ratings.show_id
 GROUP BY title ORDER BY rating DESC;
