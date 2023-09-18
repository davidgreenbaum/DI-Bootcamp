-- create table house_expenses (
-- id serial primary key,
-- date_paid date,
-- electricty float,
-- water float,
-- paid_by varchar (50)

-- );


-- insert into house_expenses (date_paid, electricty, water, paid_by)

-- values
-- ('2023-01-02', 55.3, 46.6, 'Adama'),
-- ('2023-02-01', 25.5, 62.6, 'David'),
-- ('2022-01-01', 75.5, 76.6, 'Sophie'),
-- ('2012-01-01', 74.5, 70.6, 'Ella'),
-- ('2011-01-01', 72.5, 20.6, 'Henry');

-- delete from house_expenses where electricty < 50;

delete from house_expenses where date_paid < '2019-06-06';

