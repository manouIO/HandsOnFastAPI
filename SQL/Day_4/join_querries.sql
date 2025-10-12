-- INNER JOIN return rows that are a match  accross both tables
--SELECT columns from TABLE1 INNER JOIN TABLE2 on TABLE1.COLUMN= TABLE2.COLUMN (use dot to access columns ie TABLE1.columni or TABLE2.columnj)
SELECT * from albums INNER JOIN artists on albums.AlbumId= artists.ArtistId;
SELECT albums.AlbumId,albums.Title,artists.name from albums INNER JOIN artists on albums.AlbumId= artists.ArtistId;

SELECT customers.LastName,customers.FirstName,invoices.InvoiceDate,invoices.BillingAddress,invoices.BillingCountry from customers INNER JOIN invoices on invoices.CustomerId= customers.CustomerId;

--you can remove the dot but be aware of ambiguous column names "same name in both table", so best practice is to use dot

--SELECT CustomerId, LastName, FirstName, InvoiceDate, BillingAddress, BillingCountry from customers INNER JOIN invoices on invoices.CustomerId= customers.CustomerId;

SELECT LastName, FirstName, InvoiceDate, BillingAddress, BillingCountry from customers INNER JOIN invoices on invoices.CustomerId= customers.CustomerId;

-- we can join more than 2 tables

select tracks.TrackId,tracks.Name as Trackio, albums.Title as AlbumIO, artists.Name as nameIO from tracks INNER JOIN albums on albums.AlbumId= tracks.AlbumId INNER JOIN artists on Albums.ArtistId=artists.ArtistId;

select tracks.TrackId, albums.Title as AlbumIO,tracks.Name as Trackio, tracks.Composer,artists.Name as Artist_name from tracks INNER JOIN albums on albums.AlbumId= tracks.AlbumId INNER JOIN artists on Albums.ArtistId=artists.ArtistId;


--LEFT JOIN it returns all the rows in the left table, and where there is no match in the right table, returns NULL
select  albums.ArtistId as album_artistId,artists.ArtistId as artist_artistId,artists.Name as Artist_name,albums.Title as AlbumIO from artists LEFT JOIN albums on Albums.ArtistId=artists.ArtistId;
--in this case the left table is artists, some artists don't have albums, so their albums.title and albums.ArtistId return NULL

select  albums.ArtistId as album_artistId,artists.ArtistId as artist_artistId,artists.Name as Artist_name,albums.Title as AlbumIO from albums LEFT JOIN artists on Albums.ArtistId=artists.ArtistId;
----in this case the left table is albums, all albums  have artists that own them, so there is no NULL returned on the artists TABLE.





--RIGHT JOIN

--OUTER JOIN more advanced
--CROSS JOIN