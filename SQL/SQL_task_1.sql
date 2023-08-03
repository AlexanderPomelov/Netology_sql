-- Таблица жанров

CREATE TABLE IF NOT EXISTS genres (
	genres_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL);

-- Таблица исполнителей

CREATE TABLE IF NOT EXISTS actors (
	actors_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL);

-- Таблица исполнителей и жанров(многие-ко-многим)

CREATE TABLE IF NOT EXISTS genresactors (
	genresactors_id SERIAL PRIMARY KEY,
	genres_id INTEGER NOT NULL REFERENCES genres(genres_id),
	actors_id INTEGER NOT NULL REFERENCES actors(actors_id)

);

-- Таблица альбомов

CREATE TABLE IF NOT EXISTS album (
	album_id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	year_public DATE NOT NULL);

-- Таблица альбомов и исполнителей(многие-ко-многим)
	
CREATE TABLE IF NOT EXISTS actorsalbum (
	actorsalbum_id SERIAL PRIMARY KEY,
	actors_id INTEGER NOT NULL REFERENCES actors(actors_id),
	album_id INTEGER NOT NULL REFERENCES album(album_id)
	);

--Таблица треков(один-ко-многим)

CREATE TABLE IF NOT EXISTS track (
	track_id SERIAL PRIMARY KEY,
	album_id INTEGER NOT NULL REFERENCES album(album_id),
	name VARCHAR NOT NULL,
	duration INTEGER NOT NULL);

--Таблица сборников

CREATE TABLE IF NOT EXISTS collection (
	collection_id SERIAL PRIMARY KEY,
	name VARCHAR NOT NULL,
	year_public DATE NOT NULL);
	
--Таблица треков и сборников(многие-ко-многим)

CREATE TABLE IF NOT EXISTS trackcollection (
	trackcollection_id SERIAL PRIMARY KEY,
	track_id INTEGER NOT NULL REFERENCES track(track_id),
	collection_id INTEGER NOT NULL REFERENCES collection(collection_id)
	);