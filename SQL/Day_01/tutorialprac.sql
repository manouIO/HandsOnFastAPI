-- Task 1
CREATE TABLE Products (
product_id INTEGER,
product_name VARCHAR(128),
price Decimal(10,2),
category Varchar(128),
stock_count INTEGER
);  

--Task 2
INSERT INTO Products VALUES
(1, 'Samsung 55"  TV', 12999.99, "Electronics", 25);

INSERT INTO Products VALUES
(2, 'Nike Air Max', 1899.99, "Clothing and shoes", 50);

INSERT INTO Products VALUES
(3, 'python programming book', 455, "Books", 100);

INSERT INTO Products VALUES
(4, 'Philips blender', 699, "Home & kitchen", 15);

SELECT * FROM Products WHERE product_id=2 AND stock_count=15;
DELETE FROM Products WHERE product_id=2 AND stock_count=15;
SELECT product_name, price FROM Products;

--3)
SELECT * FROM Products WHERE category='Electronics'

--Task 4
--1) update the blender price 
UPDATE Products SET price=599.00 WHERE product_name='Philips blender';

--2)update shoes price