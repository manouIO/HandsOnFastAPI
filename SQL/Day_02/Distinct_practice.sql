SELECT  * FROM artists ORDER by ArtistId ASC;

SELECT  City FROM customers ORDER by City;

SELECT DISTINCT City FROM customers ORDER by City; --all the duplicates are gone

SELECT DISTINCT Country FROM customers ORDER by Country; --all the duplicates are gone


SELECT DISTINCT City, Country FROM customers ORDER by Country ASC;

SELECT Company from customers;

SELECT DISTINCT Company from customers;

--WHERE clause for search condition

SELECT * from albums WHERE ArtistId=1;

SELECT * from tracks WHERE AlbumId=1;

select name, Milliseconds, Bytes,AlbumId FROM tracks WHERE AlbumId=1;

select name, Milliseconds, Bytes,AlbumId FROM tracks WHERE AlbumId!=1;

--other operators <,>,<=,>=, <> or !=

select name, Milliseconds, Bytes,AlbumId FROM tracks WHERE AlbumId=1 and Milliseconds>=200000;

SELECT name from tracks WHERE name like '%Ven';

--LIKE operator gives you occurences containing what you are looking for
SELECT name from tracks WHERE name like '%Door';

--IN operator

SELECT name, AlbumId FROM tracks WHERE AlbumId in (1,2,3);

SELECT name, AlbumId, GenreId FROM tracks WHERE GenreId in (9,14);


--LIMIT
SELECT name, AlbumId, GenreId FROM tracks WHERE Genreid in (9,14) LIMIT 10;

SELECT * from invoice_items ORDER by InvoiceId DESC LIMIT 5;

SELECT TrackId, name from tracks LIMIT 14 OFFSET 100; --I don't understand

SELECT name, Composer, AlbumId , Milliseconds FROM tracks WHERE AlbumId=1 ORDER by Milliseconds asc LIMIT 3;

SELECT name, Composer, AlbumId ,Bytes  FROM tracks WHERE AlbumId=4 ORDER by Bytes asc LIMIT 5;

SELECT LastName,FirstName,BirthDate FROM employees ORDER by BirthDate DESC;
--the oldest employee
SELECT LastName,FirstName,BirthDate FROM employees ORDER by BirthDate ASC LIMIT 1;
--the second oldest
SELECT LastName,FirstName,BirthDate FROM employees ORDER by BirthDate ASC LIMIT 1 OFFSET 1;
-- the two oldest
SELECT LastName,FirstName,BirthDate FROM employees ORDER by BirthDate ASC LIMIT 2 ;


--BETWEEN operator

SELECT name, AlbumId, GenreId FROM tracks WHERE GenreId BETWEEN 12 AND 14;

SELECT InvoiceId, BillingAddress, total FROM invoices WHERE total BETWEEN 1 and 5;

SELECT InvoiceId, BillingAddress, total FROM invoices WHERE total BETWEEN 15.0 and 19.0;

--the opposite

SELECT InvoiceId, BillingAddress, total FROM invoices WHERE total NOT BETWEEN 5 and 10;

SELECT InvoiceId, BillingAddress, InvoiceDate, total FROM invoices WHERE InvoiceDate BETWEEN '2010-03-01' and '2010-03-31' ORDER by InvoiceDate ASC;

SELECT InvoiceId, BillingAddress, total FROM invoices WHERE total NOT BETWEEN 15 and 19;

SELECT InvoiceId, BillingAddress, total FROM invoices WHERE total in (15,19);


--like operator

SELECT TrackId, name FROM tracks where name like "Wild%";

SELECT TrackId, name FROM tracks where name like "%Wild%";

SELECT TrackId, name FROM tracks where name like "%Wild";

SELECT TrackId, name FROM tracks where name like "%s_n%"; -- % means any number of time , _ means 1 caracter

SELECT TrackId, name FROM tracks where name like "%br_wn%";









