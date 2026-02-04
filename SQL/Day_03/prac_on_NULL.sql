

-- UNDERSTANDING MISSING INFORMATION

SELECT CustomerId , Company , Address from customers where Company is null;


SELECT CustomerId , Company , Address from customers where Company is not null;

select * from tracks where Composer is NULL;