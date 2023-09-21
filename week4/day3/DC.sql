-- PART I - i couldnt figure this out.  kept getting errors... will come back to it.


--PART II

-- CREATE TABLE Book (
-- 	id SERIAL PRIMARY KEY,
-- 	title VARCHAR (50) NOT NULL,
-- 	author VARCHAR (50) NOT NULL);

-- INSERT INTO Book (title, author)
-- VALUES ('Alice In Wonderland', 'Lewis Carroll'),
-- 	   ('Harry Potter', 'J.K. Rowling'),
-- 	   ('To Kill A Mockingbird', 'Harper Lee');

-- CREATE TABLE Student (
-- 	student_id SERIAL PRIMARY KEY,
-- 	name VARCHAR(50) NOT NULL UNIQUE,
-- 	age INTEGER CHECK (age <= 15)
-- 	);

-- INSERT INTO Student (name, age)
-- VALUES ('John', 12),
-- 	('Lera', 11),
-- 	('Patrick', 10),
-- 	('Bob', 14);

-- CREATE TABLE Library (
--     book_fk_id INTEGER,
--     student_fk_id INTEGER,
--     borrowed_date DATE,
--     PRIMARY KEY (book_fk_id, student_fk_id), -- makes sure id combinations are unique...
--     FOREIGN KEY (book_fk_id) REFERENCES Book(id) ON DELETE CASCADE ON UPDATE CASCADE, -- makes sure things stay in order as changes are made
--     FOREIGN KEY (student_fk_id) REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
-- );

-- INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
-- VALUES
--     ((SELECT id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'John'), '2022-02-15'),
--     ((SELECT id FROM Book WHERE title = 'To Kill A Mockingbird'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-03-03'),
--     ((SELECT id FROM Book WHERE title = 'Alice In Wonderland'), (SELECT student_id FROM Student WHERE name = 'Lera'), '2021-05-23'),
--     ((SELECT id FROM Book WHERE title = 'Harry Potter'), (SELECT student_id FROM Student WHERE name = 'Bob'), '2021-08-12');

-- SELECT * FROM Library;

-- SELECT S.name AS student_name, B.title AS book_title
-- FROM Library L
-- JOIN Student S ON L.student_fk_id = S.student_id
-- JOIN Book B ON L.book_fk_id = B.id;

SELECT AVG(S.age) AS average_age
FROM Library L
JOIN Student S ON L.student_fk_id = S.student_id
JOIN Book B ON L.book_fk_id = B.id
WHERE B.title = 'Alice In Wonderland';





