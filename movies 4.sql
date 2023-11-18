SELECT COUNT(id) as IMDb_rating_of_10 from movies
INNER JOIN ratings ON movies.id = ratings.movie_id
WHERE ratings.rating = 10.0;
