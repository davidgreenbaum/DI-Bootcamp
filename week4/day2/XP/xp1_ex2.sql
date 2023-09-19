-- select * from customer;

-- select (first_name, last_name) as full_name from customer;

-- SELECT DISTINCT create_date FROM customer;

-- SELECT * FROM customer ORDER BY first_name DESC;

-- SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate;

-- SELECT address, phone FROM address WHERE district = 'Texas';

-- select * from film WHERE film_id in (15, 150) ;

-- SELECT film_id, title, description, length, rental_rate from film WHERE title = 'Shawshank Redemption';

-- SELECT film_id, title, description, length, rental_rate FROM film WHERE LOWER(TRIM(title)) LIKE 'sh%';

-- SELECT film_id, title, rental_rate FROM film ORDER BY rental_rate DESC LIMIT 10;

-- SELECT film_id, title, rental_rate FROM film ORDER BY rental_rate DESC LIMIT 10 OFFSET 10;

-- SELECT 
-- 	c.first_name, c.last_name, p.amount, p.payment_date
-- FROM 
-- 	customer AS c 
-- JOIN 
-- 	payment AS p 
-- ON 
-- 	c.customer_id = p.customer_id
-- ORDER BY 
-- 	c.customer_id;

-- SELECT f.film_id, f.title 
-- FROM film f
-- LEFT JOIN inventory i ON f.film_id = i.film_id
-- WHERE i.film_id IS NULL;

SELECT c.country, ci.city
FROM country c
INNER JOIN city ci ON c.country_id = ci.country_id;



