--Задание 2.1.

SELECT  name_track, duration  FROM track
ORDER BY duration DESC
LIMIT 1;

--Задание 2.2.

SELECT name_track, duration  FROM track
WHERE duration >= '00:03:30';

--Задание 2.3.

SELECT collection, year_public FROM collection
WHERE year_public BETWEEN 2018 AND 2020;

--Задание 2.4.

SELECT name FROM actors
WHERE name NOT LIKE ('% %');

--Задание 2.5.

SELECT name_track FROM track
WHERE 'мой' = ANY(string_to_array(lower(name_track), ' ')) OR
      'my' = ANY(string_to_array(lower(name_track), ' '));

--Задание 3.1.

SELECT name_genres, COUNT(name_genres) FROM genresactors ga
JOIN genres g ON g.genres_id = ga.genres_id 
GROUP BY name_genres;

--Задание 3.2.

SELECT COUNT(track_id) FROM track t 
JOIN album a  ON a.album_id = t.album_id 
WHERE year_public BETWEEN 2019 and 2020; 

--Задание 3.3.

SELECT name_album, AVG(duration) FROM track t
JOIN album a ON a.album_id = t.album_id
GROUP BY name_album
ORDER BY avg;

--Задание 3.4.

SELECT name FROM actors a 
WHERE name NOT IN (
    SELECT name FROM actors a2 
    JOIN actorsalbum ab ON a2.actors_id = ab.actors_id  
	JOIN album a3 ON ab.album_id = a3.album_id 
    WHERE year_public = 2020
);

--Задание 3.5.

SELECT name_collection, trackcollection_id, name FROM collection c
JOIN trackcollection t ON c.collection_id = t.collection_id
JOIN track tr ON tr.track_id = t.track_id 
JOIN album a ON a.album_id = tr.album_id 
JOIN actorsalbum ab ON ab.album_id  = a.album_id  
JOIN actors ac ON ac.actors_id = ab.actors_id 
WHERE name = 'The Beatles';
 
--Задание 4.1.

SELECT DISTINCT name_album 
FROM album a  
JOIN actorsalbum a2 ON a.album_id = a2.album_id 
JOIN actors a3 ON a2.actors_id = a3.actors_id  
JOIN genresactors g ON a3.actors_id =g.actors_id 
GROUP BY name_album, g.actors_id  
HAVING COUNT(genres_id) > 1; 

--Задание 4.2.

SELECT name_track FROM track t
FULL OUTER JOIN trackcollection t2 ON t2.track_id = t.track_id
WHERE t2.track_id IS NULL;


--Задание 4.3.

SELECT name 
FROM actors a 
JOIN actorsalbum ab  ON ab.actors_id  = a.actors_id  
JOIN album a2  ON a2.album_id  = ab.album_id  
JOIN track t  ON t.album_id  = a2.album_id  
WHERE duration = ( 
SELECT MIN(duration) FROM track t2  
JOIN actorsalbum a3  ON a3.album_id = t2.album_id
);


--Задание 4.4.

SELECT name_album 
FROM album a  
JOIN track t ON t.album_id  = a.album_id  
GROUP BY a.album_id 
HAVING COUNT(name_track) = ( 
SELECT COUNT(track_id) FROM track t2 
GROUP BY album_id  
ORDER BY 1 
LIMIT 1 
);