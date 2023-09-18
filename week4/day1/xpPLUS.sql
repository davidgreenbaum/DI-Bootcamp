-- create table students (
-- id serial primary key,
-- last_name varchar, 
-- first_name varchar, 
-- birth_date date);


-- insert into students (last_name, first_name, birth_date)

-- values
-- ('Benichou','Marc', '1998-11-02'),
-- ('Cohen', 'Yoan', '2010-12-03'),
-- ('Benichou', 'Lea', '1987-07-27'),
-- ('Dux', 'Amelia', '1996-04-07'),
-- ('Grez', 'David', '2003-06-14');

-- select * from students;

-- select first_name, last_name from students

-- select first_name, last_name from students where id = 2;

-- select first_name, last_name from students where first_name = 'Marc' and last_name = 'Benichou';

-- select first_name, last_name from students where first_name = 'Marc' or last_name = 'Benichou';

-- select first_name from students where first_name LIKE '%a%';

-- select first_name from students where first_name LIKE 'A%';

-- select first_name from students where first_name LIKE '%a';

-- select first_name from students where SUBSTRING (first_name, LENGTH(first_name) -1, 1) ILIKE 'a';

-- select * from students where id in (1, 3);

select * from students where birth_date >= '2000-01-01';