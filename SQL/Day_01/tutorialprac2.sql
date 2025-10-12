CREATE TABLE Product (
product_id INTEGER PRIMARY KEY AUTOINCREMENT,
product_name VARCHAR(128),
price Decimal(10,2),
category Varchar(128),
stock_count INTEGER
);  

--Task 2
INSERT INTO Product (product_name,price,category,stock_count) VALUES
('Hisense 55"  TV', 12999.99, "Electronics", 25);