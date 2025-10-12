SELECT * FROM artists order by ArtistId ASC;


-- Distinct clauses
SELECT city from customers order by  City;

select DISTINCT City from customers order by city;

select Country from customers order by Country;

select DISTINCT Country from customers order by Country;

select City , Country from customers order by Country;

select DISTINCT City , Country from customers order by Country;

select Company from customers;

select DISTINCT Company from customers;


-- WHERE clauses FOR SEARCH CONDITION

select * from albums where ArtistId = 1;

select * from albums where ArtistId = 5;

select * from tracks where AlbumId = 1;

select name , Milliseconds, Bytes, AlbumId from tracks where AlbumId = 1;

select name , Milliseconds, Bytes, AlbumId from tracks where AlbumId <> 1;
-- Other operators  < , > , <= , >= ,     != or <>


select name , Milliseconds, Bytes, AlbumId from tracks where AlbumId = 1 and Milliseconds > 200000;

select name from tracks where name like 'Door%';


select name, AlbumId  from tracks where AlbumId in (1, 2, 3);

-- isaka  

select name, AlbumId , GenreId from tracks where GenreId IN (9,14);

-- 