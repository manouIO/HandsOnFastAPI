LIMIT

select name, AlbumId , GenreId from tracks where GenreId IN (9,14) LIMIT 10;

SELECT * FROM invoice_items ORDER BY InvoiceId DESC LIMIT 5;

SELECT TrackId , name FROM tracks LIMIT 14;

SELECT TrackId , name from tracks LIMIT 14 OFFSET 100;

select name, Composer , AlbumId  , Milliseconds FROM tracks WHERE AlbumId = 1 ORDER BY Milliseconds asc limit 3; 

SELECT NAME, Composer , AlbumId , Bytes FROM tracks WHERE AlbumId=4 ORDER  BY Bytes DESC LIMIT 5;

SELECT LastName , FirstName , BirthDate from employees order by BirthDate asc limit 1 OFFSET 1;
SELECT LastName , FirstName , BirthDate from employees order by BirthDate asc limit 2;


-- BETWEEN  :  test_expression BETWEEN low_expression AND high_expression

SELECT InvoiceId , BillingAddress , Total  from invoices where total BETWEEN 15.0 AND 19.0 ;


SELECT InvoiceId , BillingAddress , Total  from invoices where total NOT BETWEEN 15.0 AND 19.0 ;


SELECT InvoiceId , BillingAddress ,InvoiceDate , Total from invoices where InvoiceDate BETWEEN '2010-03-01' AND '2010-03-31' ORDER BY InvoiceDate asc;

SELECT InvoiceId , BillingAddress ,InvoiceDate , Total from invoices where InvoiceDate not BETWEEN '2010-03-01' AND '2010-03-31' ORDER BY InvoiceDate asc;


SELECT InvoiceId , BillingAddress , Total  from invoices where total in (15.0 , 19.0);


-- like

-- '%ag'  will match  bag, jag, goulag , mag , catchag,  but will  not match gatchou, 

-- '%it%' will match culprit, it, italy , coity , choit. 

-- '_ar'  will match jar, car, bar, dar, mar, nar, BUT WILL NOT MATCH blar, cargo, 

select TrackId , name from tracks where name LIKE "Wild%";

select TrackId , name from tracks where name LIKE "%Wild";

select TrackId , name from tracks where name LIKE "%Wild%";

select TrackId , name from tracks where name LIKE "s_n";

select TrackId , name from tracks where name LIKE "%s_n%";

select TrackId , name from tracks where name LIKE "%br_wn%";  -- LIKE is not case sensitive




