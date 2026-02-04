

CREATE TABLE discount_summary ( reduction VARCHAR(128));


INSERT INTO  discount_summary ( reduction) values ('20 percent') , ('24% decrease'),('6% last year') , ('24_o this year');

select reduction from discount_summary;


-- Here I am looking for any records from the reduction field that starts with the character 2
select reduction from discount_summary where reduction like "2%";

-- Now , I am looking for any record that ends with the characters 'ar';
select reduction from discount_summary where reduction like "%ar";

-- Now , lets look for any record that contains the letter 'e';
select reduction from discount_summary where reduction like "%e%";


select reduction from discount_summary where reduction like "%\%%" escape "\";

select reduction from discount_summary where reduction like "%@%%" escape "@";

select reduction from discount_summary where reduction like "%@_%" escape "@";

select reduction from discount_summary where reduction like "%$_%" escape "$";



