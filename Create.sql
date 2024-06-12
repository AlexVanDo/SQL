CREATE TABLE Genres (
	id SERIAL PRIMARY KEY,
	genre VARCHAR(60) NOT NULL
);

CREATE TABLE Autors(
	id SERIAL PRIMARY KEY,
	musician VARCHAR(60) NOT NULL,
	name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS genres_autors (
	genre_id INTEGER REFERENCES genres(id),
	autor_id INTEGER REFERENCES autors(id),
	CONSTRAINT ga PRIMARY KEY (genre_id, autor_id)
);

CREATE TABLE Albums(
	id SERIAL PRIMARY KEY,
	album VARCHAR(60) NOT NULL,
	year INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS albums_autors (
	album_id INTEGER REFERENCES albums(id),
	autor_id INTEGER REFERENCES autors(id),
	CONSTRAINT aa PRIMARY KEY (album_id, autor_id)
);

CREATE TABLE IF NOT EXISTS Tacks (
	id SERIAL PRIMARY KEY,
	album_id INTEGER NOT NULL REFERENCES Albums(id),
	track_name VARCHAR(60) NOT NULL,
	duration_sec INTEGER NOT NULL
);

CREATE TABLE Collection (
	id SERIAL PRIMARY KEY,
	collection_name VARCHAR(60) NOT NULL,
	YEAR INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS collection_tracks (
	collection_id INTEGER REFERENCES collection(id),
	track_id INTEGER REFERENCES tracks(id),
	CONSTRAINT ct PRIMARY KEY (collection_id, track_id)
);

