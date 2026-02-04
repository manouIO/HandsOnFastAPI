--select 
--select query
select * from Products;
select name, id, price from products order by price asc;

-- renaming for display purpose (not permanently)
select name as nom, id as produit_id, price as prix from products;

--filter with where 
select name, id, price, inventory from products WHERE inventory=0;

--operators =,>,<,>=,<=

select name, id, price, inventory from products WHERE price>=60;

--NOT operator

select name, id, price, inventory from products WHERE price!=60;

-- AND, OR query
select name, id, price, inventory from products WHERE price!=60 and inventory>=10;
select name, id, price, inventory from products WHERE price!=60 or inventory>=70;

--IN operator
Select * from products where id in (1,2,3);

select * from products;

--like operator
SELECT * FROM products WHERE name LIKE '%TV%';

--Ordering
select name as nom, id as produit_id, price as prix from products order by price DESC;

select name, id , price, inventory from products order by price DESC, inventory ASC;


--LIMIT OFFSET

select * from products LIMIT 5;
select * from products where price>=9 LIMIT 6;

--use offset to skip n numbers of rows
select * from products where price>=9 LIMIT 5 OFFSET 3;


--inserting data

INSERT INTO products (name,price,inventory) VALUES ('tortillas', 4,1000), ('mango', 10,100), ('bike', 2300,50) returning *;

--Deleting data

INSERT INto products (name, price, inventory) VALUES ('blabla',23,31) returning *;

DELETE FROM products where id=25 RETURNING *;
select * from products where id=25;


-- Updating data
select * from products;
UPDATE products SET name='ndole lave', price=40 WHERE id=23 returning *;
select * from products;



