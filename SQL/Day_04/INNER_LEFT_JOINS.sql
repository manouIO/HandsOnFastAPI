-- INNER JOIN
SELECT list_columns FROM table_1 INNER JOIN table_2 ON table_1.column = table_2.column


Select posts.text , users.name from Post INNER JOIN Users ON Posts.user_id = Users.user_id;

SELECT albums.Title , artists.Name from albums INNER JOIN artists on albums.ArtistId = artists.ArtistId;

SELECT customers.FirstName , customers.LastName , customers.Company , invoices.BillingCity 
, invoices.BillingCountry  from customers inner JOIN invoices on invoices.CustomerId = customers.CustomerId;


SELECT TrackId , name , title from tracks inner join albums on albums.AlbumId = tracks.AlbumId;

SELECT  tracks.AlbumId , tracks.TrackId , tracks.name , albums.AlbumId, albums.title from tracks inner join albums on albums.AlbumId = tracks.AlbumId;



select tracks.TrackId , tracks.Name as trackIO,  albums.Title as albumIO  ,
 artists.name AS nameIO from tracks INNER JOIN albums on albums.AlbumId = tracks.AlbumId inner join artists on  artists.ArtistId = albums.ArtistId ;


select tracks.TrackId , tracks.Name as trackIO,  albums.Title as albumIO  ,
 artists.name AS nameIO , artists.ArtistId as artistIO from tracks INNER JOIN albums on albums.AlbumId = tracks.AlbumId 
inner join artists on  artists.ArtistId = albums.ArtistId where artists.ArtistId = 3 ;

-- LEFT JOIN


select artists.ArtistId , artists.Name , albums.AlbumId , albums.Title from artists left join albums on albums.ArtistId = artists.ArtistId WHERE albums.AlbumId IS NULL;


select artists.ArtistId , artists.Name , albums.AlbumId , albums.Title from artists left join albums on albums.ArtistId = artists.ArtistId WHERE albums.AlbumId IS NULL;
