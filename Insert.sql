INSERT INTO GENRES (genre) values('Rock');
INSERT INTO GENRES (genre) values('Pop');
INSERT INTO GENRES (genre) values('Jazz');

INSERT INTO AUTORS (musician, "name") values('исп1', 'Антон');
INSERT INTO AUTORS (musician, "name") values('исп2', 'София');
INSERT INTO AUTORS (musician, "name") values('исп3', 'Курт');
INSERT INTO AUTORS (musician, "name") values('исп4', 'Жора');
INSERT INTO AUTORS (musician, "name") values('исп5', 'Картоха');
INSERT INTO AUTORS (musician, "name") values('исп6', 'Кабан');

INSERT INTO  genres_autors VALUES (1, 1), (1, 2), (1, 3), (2, 2), (3, 4);

INSERT INTO ALBUMS (album , "year") values('Железяки', 2015);
INSERT INTO ALBUMS (album , "year") values('Капризуля', 2007);
INSERT INTO ALBUMS (album , "year") values('Дай мне умереть', 2020);

INSERT INTO  albums_autors VALUES (1, 1), (1, 2), (2, 2), (3, 3), (3, 2);

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

INSERT INTO Collection (collection_name , "year") values('ТОП треки', 2023);
INSERT INTO Collection (collection_name , "year") values('Для души', 2022);
INSERT INTO collection (collection_name, "year") VALUES('Любимые', 2018);
INSERT INTO collection (collection_name, "year") VALUES('По кайфу', 2020);

INSERT INTO  collection_tracks VALUES (1, 1), (1, 2), (1, 4), (1, 5), (2, 3), (2, 4), (2, 7), (2, 8);
INSERT INTO collection_tracks VALUES (3, 6), (3, 7), (3, 8), (3, 9), (4, 1), (4, 5), (4, 6), (4, 9);
