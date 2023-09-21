--EXERCISE 1

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

--EXERCISE 2

-- UPDATE film
-- SET language_id = 2
-- WHERE film_id = 133

-- 2. customer_id, i believe it will insure that the primary key of the table we are inserting into will correspond correctly with the data being inserted

-- 3. i think you have to make sure its not referenced by other tables?

-- SELECT COUNT(*) AS num_unreturned_dvds
-- FROM rental
-- WHERE return_date IS NULL;


--couldnt figure this out...
-- SELECT rental.rental_id, rental.rental_date, payment.amount, film.title
-- FROM rental
-- JOIN payment ON rental.rental_id = payment.rental_id
-- JOIN film ON rental.rental_id = film.film_id
-- WHERE rental.return_date IS NULL
-- ORDER BY payment.amount DESC
-- LIMIT 30;

-- SELECT film.title
-- FROM film
-- JOIN film_actor ON film.film_id = film_actor.film_id
-- JOIN actor ON film_actor.actor_id = actor.actor_id
-- WHERE actor.first_name = 'Penelope'
-- AND actor.last_name = 'Monroe'
-- AND film.description LIKE '%sumo wrestler%';

-- SELECT film.title
-- FROM film
-- JOIN film_category ON film.film_id = film_category.film_id
-- JOIN category ON film_category.category_id = category.category_id
-- WHERE category.name = 'Documentary'
-- AND film.length < 60
-- AND film.rating = 'R';




