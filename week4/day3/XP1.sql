-- SELECT * FROM language;

-- SELECT 
-- 	film.title, film.description, language.name
-- FROM
-- 	film
-- INNER JOIN
-- 	language ON film.language_id = language.language_id;


-- SELECT film.title, film.description, language.name
-- FROM language
-- LEFT JOIN
-- 	film ON language.language_id = film.language_id;

-- CREATE TABLE new_film (
-- 	id SERIAL PRIMARY KEY,
-- 	name VARCHAR(255) NOT NULL
-- );

-- INSERT INTO new_film (name) VALUES ('Running On Empty');
-- INSERT INTO new_film (name) VALUES ('Barbie');
-- INSERT INTO new_film (name) VALUES ('Wedding Crashers');
-- INSERT INTO new_film (name) VALUES ('The Mask');
-- INSERT INTO new_film (name) VALUES ('Ace Ventura');

-- CREATE TABLE customer_review (
-- 	review_id SERIAL PRIMARY KEY,
-- 	film_id INTEGER NOT NULL REFERENCES new_film(id) ON DELETE CASCADE,
-- 	language_id INTEGER NOT NULL REFERENCES language(language_id),
-- 	title VARCHAR(255) NOT NULL,
-- 	score INTEGER NOT NULL CHECK (score BETWEEN 1 AND 10),
-- 	review_text TEXT NOT NULL,
-- 	last_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)

-- INSERT INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES (4, 1, 'The Mask', 10, 'I laughed the whole time!');
-- INSERT INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES (5, 1, 'Ace Ventura', 9, 'Funniest movie ive ever seen!');
-- COMMIT;

-- DELETE FROM new_film WHERE id = 4;

-- SELECT * FROM new_film;