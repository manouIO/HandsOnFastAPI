

select TrackId , name from tracks where name LIKE "Wild%";


-- THis will match all the records starting with Uppercase W , followed by 'ild' and followed by any character any number of times
select TrackId , name from tracks where name glob "Wild*";

-- THis will match all the records starting with lowercase 'wild' and followed by any character any number of times
select TrackId , name from tracks where name glob "wild*";


select TrackId , name from tracks where name glob "Br?k*"; -- will match Broke, Broken, NOT Break

select TrackId , name from tracks where name glob "[BCD]*";

select TrackId , name from tracks where name glob "[a-zA-Z0-9]*";

select TrackId , name from tracks where name glob "[0-2]*";


select TrackId , name from tracks where name glob "[^a-zA-Z]*";

select TrackId , name from tracks where name glob "[^a-zA-Z0-9]*";

select TrackId , name  from tracks where name glob "[A-Z]?[0-9]*"; --Zi2 , P90 , C#2





