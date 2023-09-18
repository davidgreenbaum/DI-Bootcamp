-- create table items (
-- id serial primary key,
-- item_name varchar,
-- price float)

-- insert into items (item_name, price)
-- values
-- ('Small Desk', 100),
-- ('Large Desk', 300),
-- ('Fan', 80);

-- create table customers (
-- id serial primary key,
-- first_name varchar, 
-- last_name varchar)

-- insert into customers (first_name, last_name)
-- values
-- ('Greg', 'Jones'),
-- ('Sandra', 'Jones'),
-- ('Scott', 'Scott'),
-- ('Trevor', 'Green'),
-- ('Melanie', 'Johnson')

-- select * from items;

-- select * from items where price > 80

-- select * from items where price <= 300;

-- select * from customers where last_name = 'Smith';

-- select * from customers where last_name = 'Jones';

select * from customers where last_name != 'Scott';

