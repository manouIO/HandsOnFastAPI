-- Task 1

CREATE TABLE Products (
product_id INTEGER,
product_name VARCHAR(128),
price DECIMAL(10,2),
category VARCHAR(128),
stock_count INTEGER
);

-- Task 2

INSERT INTO Products VALUES
(1, 'Samsung 55" TV', 12999.99,  'Electronics', 25);

INSERT INTO Products VALUES 
(2 , 'Nike Air Max' , 1899.99, 'Clothing and Shoes', 50);

INSERT INTO Products VALUES 
( 3, 'Python Programming Book', 455.50 , 'Books', 100);

INSERT INTO Products VALUES 
( 4, 'Philips Blender', 699.00, 'Home and Kitchen', 15);


-- Task 3
--1)
SELECT * from Products;

--2)
SELECT product_name, price from Products;

--3)
select * from Products WHERE category = 'Electronics';


-- Task 4
--1)

UPDATE Products SET price = 599.00 where product_name = 'Philips Blender';
