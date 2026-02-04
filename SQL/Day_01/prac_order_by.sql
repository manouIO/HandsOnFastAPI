--SELECT    select_list  FROM    table  ORDER BY     column_1 ASC,     column_2 DESC;


select name, Milliseconds , AlbumId from tracks;

select name, Milliseconds , AlbumId from tracks order by AlbumId ASC;

select name, Milliseconds , AlbumId from tracks order by AlbumId desc;


select name, Milliseconds , AlbumId from tracks order by AlbumId asc,  Milliseconds desc;

select name , Milliseconds , AlbumId from tracks order by 3 , 2 ;
-- 9999 , 0000 , "" , NULL

select * from tracks where Composer is null ;

select TrackId , name  , Composer from tracks order by Composer nulls;

select TrackId , name  , Composer from tracks order by Composer nulls last;

