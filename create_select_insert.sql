CREATE TABLE Genres (
	id SERIAL PRIMARY KEY,
	genre VARCHAR(60) NOT NULL
);

insert into GENRES (genre) values('Rock');
insert into GENRES (genre) values('Pop');
insert into GENRES (genre) values('Jazz');

CREATE TABLE Autors(
	id SERIAL PRIMARY KEY,
	musician VARCHAR(60) NOT NULL,
	name VARCHAR(60) NOT NULL
);

insert into AUTORS (musician, "name") values('исп1', 'Антон');
insert into AUTORS (musician, "name") values('исп2', 'София');
insert into AUTORS (musician, "name") values('исп3', 'Курт');
insert into AUTORS (musician, "name") values('исп4', 'Жора');
insert into AUTORS (musician, "name") values('исп5', 'Картоха');
insert into AUTORS (musician, "name") values('исп6', 'Кабан');

CREATE TABLE IF NOT EXISTS genres_autors (
	genre_id INTEGER REFERENCES genres(id),
	autor_id INTEGER REFERENCES autors(id),
	CONSTRAINT ga PRIMARY KEY (genre_id, autor_id)
);

INSERT INTO  genres_autors VALUES (1, 1), (1, 2), (1, 3), (2, 2), (3, 4);

CREATE TABLE Albums(
	id SERIAL PRIMARY KEY,
	album VARCHAR(60) NOT NULL,
	year INTEGER NOT NULL
);

insert into ALBUMS (album , "year") values('Железяки', 2015);
insert into ALBUMS (album , "year") values('Капризуля', 2007);
insert into ALBUMS (album , "year") values('Дай мне умереть', 2020);

CREATE TABLE IF NOT EXISTS albums_autors (
	album_id INTEGER REFERENCES albums(id),
	autor_id INTEGER REFERENCES autors(id),
	CONSTRAINT aa PRIMARY KEY (album_id, autor_id)
);

INSERT INTO  albums_autors VALUES (1, 1), (1, 2), (2, 2), (3, 3), (3, 2);

CREATE TABLE IF NOT EXISTS Tacks (
	id SERIAL PRIMARY KEY,
	album_id INTEGER NOT NULL REFERENCES Albums(id),
	track_name VARCHAR(60) NOT NULL,
	duration_sec INTEGER NOT NULL
);

INSERT INTO tracks (album_id, track_name, duration_sec) VALUES (1, 'Роботы', 253);
INSERT INTO tracks (album_id, track_name, duration_sec) VALUES (1, 'Стальца', 226);
INSERT INTO tracks (album_id, track_name, duration_sec) VALUES (1, 'Золотые руки', 282);
INSERT INTO tracks (album_id, track_name, duration_sec) VALUES (2, 'Не буду', 132);
INSERT INTO tracks (album_id, track_name, duration_sec) VALUES (2, 'Дай мне всё', 182);
INSERT INTO tracks (album_id, track_name, duration_sec) VALUES (2, 'Нет', 116);
INSERT INTO tracks (album_id, track_name, duration_sec) VALUES (3, 'Дождь', 267);
INSERT INTO tracks (album_id, track_name, duration_sec) VALUES (3, 'Прощай', 234);
INSERT INTO tracks (album_id, track_name, duration_sec) VALUES (3, 'Слепой мир', 212);
INSERT INTO tracks (album_id, track_name, duration_sec) VALUES (3, 'Мой пульс', 222);

CREATE TABLE Collection (
	id SERIAL PRIMARY KEY,
	collection_name VARCHAR(60) NOT NULL,
	YEAR INTEGER NOT NULL
);

INSERT INTO Collection (collection_name , "year") values('ТОП треки', 2023);
INSERT INTO Collection (collection_name , "year") values('Для души', 2022);
INSERT INTO collection (collection_name, "year") VALUES('Любимые', 2018);
INSERT INTO collection (collection_name, "year") VALUES('По кайфу', 2020);

CREATE TABLE IF NOT EXISTS collection_tracks (
	collection_id INTEGER REFERENCES collection(id),
	track_id INTEGER REFERENCES tracks(id),
	CONSTRAINT ct PRIMARY KEY (collection_id, track_id)
);

INSERT INTO  collection_tracks VALUES (1, 1), (1, 2), (1, 4), (1, 5), (2, 3), (2, 4), (2, 7), (2, 8);
INSERT INTO collection_tracks VALUES (3, 6), (3, 7), (3, 8), (3, 9), (4, 1), (4, 5), (4, 6), (4, 9);

--Название и продолжительность самого длительного трека
SELECT track_name, duration_sec FROM tracks
WHERE duration_sec IN (SELECT MAX(duration_sec) FROM tracks);

--Название треков, продолжительность которых не менее 3,5 минут(210 секунд)
SELECT track_name FROM tracks
WHERE duration_sec >= 210;

--Названия сборников, вышедших в период с 2018 по 2020 год включительно
SELECT collection_name, year FROM collection
WHERE year BETWEEN 2018 AND 2020;

--Исполнители, чьё имя состоит из одного слова
SELECT musician, name FROM autors
WHERE name NOT LIKE '% %';

--Название треков, которые содержат слово «мой» или «my»
SELECT track_name FROM tracks
WHERE lower(track_name) LIKE '%мой%' OR lower(track_name) LIKE '%my%';

--Количество исполнителей в каждом жанре
SELECT genre, count(genre)  FROM genres g
JOIN genres_autors ga ON g.id = ga.genre_id
GROUP BY genre;

--Количество треков, вошедших в альбомы 2019–2020 годов
SELECT track_name FROM tracks t 
JOIN albums a ON t.album_id = a.id 
WHERE a."year" BETWEEN 2019 AND 2020; 

--Средняя продолжительность треков по каждому альбому
SELECT avg(duration_sec)  FROM tracks t;

--Все исполнители, которые не выпустили альбомы в 2020 году
SELECT DISTINCT("name")  FROM autors a
JOIN albums_autors aa ON a.id = aa.autor_id 
JOIN albums a2 ON aa.album_id = a2.id 
WHERE a2."year" != 2020;

--Названия сборников, в которых присутствует конкретный исполнитель
SELECT DISTINCT(collection_name) FROM collection c
JOIN collection_tracks ct ON c.id = ct.collection_id 
JOIN tracks t ON ct.track_id = t.id 
JOIN albums al ON al.id = t.album_id 
JOIN albums_autors aa ON al.id = aa.album_id 
JOIN autors au ON au.id = aa.autor_id 
WHERE au."name" LIKE 'Курт';

--