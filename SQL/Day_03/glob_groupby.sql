--Missing informations

SELECT * FROM customers;

SELECT CustomerId, LastName, Company, Country FROM customers WHERE Company is NULL;

SELECT CustomerId, LastName, Company, Country FROM customers WHERE PostalCode is NULL;

--glob operator is case sensitive
SELECT TrackId, Name from tracks where Name glob "wild*"; --no occurences with lower w

SELECT TrackId, Name from tracks where Name glob "Wild*";


SELECT TrackId, Name from tracks where Name glob "*anc?s*"; --? means one caracter

SELECT TrackId, Name from tracks where Name glob "[BCD]*"; --[BCD] means start with B C or D

SELECT TrackId, Name from tracks where Name glob "[0-6]*"; --[0-n] means start with 0 1 up to n,

SELECT * FROM tracks;


SELECT TrackId, name from tracks where name glob "[a-zA-Z0-9]*" --a-z means start with any letter lower case, 
--A-Z means start with any letter upper case, 0-9 means start with any number


SELECT * FROM tracks WHERE AlbumId=1 ;
SELECT avg(Milliseconds) FROM tracks WHERE AlbumId=1 ;

SELECT  AlbumId, avg(Milliseconds) FROM tracks GROUP by AlbumId ;

SELECT  AlbumId, round(avg(Milliseconds),2) avg_length FROM tracks GROUP by AlbumId ;

SELECT  AlbumId, count(Milliseconds) count_albums FROM tracks GROUP by AlbumId ;

SELECT  AlbumId, name, Composer, max(Milliseconds) longest_track FROM tracks GROUP by AlbumId  order by longest_track ASC;




