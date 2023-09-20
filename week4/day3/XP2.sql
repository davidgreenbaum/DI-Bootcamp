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




