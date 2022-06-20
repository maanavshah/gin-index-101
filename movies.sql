CREATE TABLE movies(
id  SERIAL PRIMARY KEY,
title varchar(255) NOT NULL,
year INT,
metascore INT
);

SELECT count(*) from movies;

SELECT * from movies LIMIT 10;

EXPLAIN ANALYSE SELECT * FROM movies where title like 'Pirate%';

EXPLAIN ANALYSE SELECT * FROM movies where title ilike 'Pirate%';

EXPLAIN ANALYSE SELECT * FROM movies where title ilike '%sea%';

CREATE INDEX movies_name_idx_0 ON movies (title);

EXPLAIN ANALYSE SELECT * FROM movies where title like 'Pirate%';

EXPLAIN ANALYSE SELECT * FROM movies where title ilike 'Pirate%';

EXPLAIN ANALYSE SELECT * FROM movies where title ilike '%sea%';

DROP INDEX movies_name_idx_0;

CREATE INDEX movies_name_idx_1 ON movies USING GIN (to_tsvector('english', title));

EXPLAIN ANALYZE SELECT *
FROM movies
WHERE to_tsvector('english', title) @@ to_tsquery('english', 'sea');

DROP INDEX movies_name_idx_1;
