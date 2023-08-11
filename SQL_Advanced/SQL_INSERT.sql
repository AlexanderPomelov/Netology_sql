--Наполнение таблицы исполнителей

INSERT INTO actors(name)
VALUES ('The Beatles'),
	   ('Michael Jackson'),
	   ('Elvis Presley'),
	   ('Elton Jhon'),
	   ('Madonna');
	   
--Наполнение таблицы жанров
	   
INSERT INTO genres (name)
VALUES ('Rock'),
	   ('Pop'),
	   ('Dance'),
	   ('Folk'),
	   ('Jazz');
	  
--Наполнение таблицы жанров-исполнителей
	  
INSERT INTO genresactors(genres_id, actors_id)
VALUES 	(1, 1), (1, 4), (1, 5),
		(2, 2), (2, 3), (2, 5),
		(3,2),
		(4,5),
		(5,5);
		
		
	   
--Наполнение таблицы альбомов
	   
INSERT INTO album (name, year_public)
VALUES ('Help!', 1965),('Revolver', 1966),
	   ('Forever, Michael', 1975),('Bad', 1987),
	   ('Harum Scarum',1965),('Spinout' , 1966),
	   ('Captain Fantastic and the Brown Dirt Cowboy', 1975), ('Caribou', 1974),
	   ('Madame X', 2019), ('Rebel Heart', 2015);
	  
--Наполнение таблицы исполнителей-альбомов

INSERT INTO actorsalbum (actors_id, album_id)
VALUES 	(1, 1), (1, 2),
		(2, 3), (2, 4),
		(3, 5), (3, 6),
		(4, 7), (4, 8),
		(5, 9), (5, 10);
	   
--Наполнение таблицы треков
	  
INSERT INTO track (album_id, name, duration)
VALUES 	(1, 'Help!', '00:02:16'), (1, 'The Night Before', '00:02:30'), (1, 'Another Girl', '00:02:02'),
	   	(2, 'Taxman', '00:02:39'), (2, 'Love You To', '00:03:01'), (2, 'Yellow Submarine', '00:02:42'),
		(3, 'Were Almost There', '00:03:41'), (3, 'Take Me Back', '00:03:29') , (3, 'Dapper Dan', '00:03:08'),
		(4, 'Bad', '00:04:07'), (4, 'Another Part of Me', '00:03:54'), (4, 'Dirty Diana', '00:04:52'),
		(5, 'Harlem Holiday', '00:02:18'), (5, 'My Desert Serenade' , '00:01:47'), (5, 'Mirage', '00:02:25'),
		(6, 'Stop, Look And Listen', '00:01:31'), (6, 'Adam and Evil', '00:01:55'), (6, 'All That I Am', '00:02:15'),
		(7, 'Captain Fantastic and the Brown Dirt Cowboy', '00:05:46'), (7, 'Tower of Babel', '00:04:28'),
		(8, 'Pinky', '00:03:54'), (8, 'Grimsby', '00:03:47'),
		(9, 'Dark Ballet', '00:04:14'), (9, 'God Control', '00:06:19'),
		(10, 'Living for Love', '00:03:38'), (10, 'Devil Pray', '00:04:05');
	   
	   
--Наполнение таблицы сборников

INSERT INTO collection (name, year_public)
VALUES 	('1', 1999), ('Yellow Submarine Songtrack', 2000),
		('One Day in Your Life', 1981), ('Anthology', 1986),
		('50,000,000 Elvis Fans Can’t Be Wrong', 1959), ('Elvis for Everyone!', 1965),
		('Your Songs', 1985), ('To Be Connected', 1990),
		('Finally Enough Love: 50 Number Ones', 2020), ('Celebration', 2009);
		
--Наполнение таблицы треков-сборников
	
INSERT INTO trackcollection (track_id, collection_id)
VALUES 	(1, 1), (6, 1), (6, 2), (5, 2),
		(8, 3),
		(25, 9);
