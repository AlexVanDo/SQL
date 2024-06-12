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