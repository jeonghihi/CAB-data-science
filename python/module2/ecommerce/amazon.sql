
-- Basic commands:
-- SHOW COLUMNS FROM sales;
-- show databases;
-- use ecom;
-- show tables from ecom;
-- select *from sales;

# show columns from product_summary in ecom;

-- how to combine ‘total_sales per country’ from sales database and ‘rating/review_count’ from monitor database into one table,
-- and then set the index for this table as 'invoice date' from sales database

use ecom;
select sales.InvoiceDate as invoice, 
		monitor_sales.review_count as revier_count, 
        Country, 
        Description
from (sales inner join monitor_sales on sales.Description = monitor_sales.title)
group by InvoiceDate, Country;

--
SELECT continent, name, area,
  avg(area) over (partition by continent) as avg_area_overContinent
FROM world

-- this method takes too much time
use ecom;
select sales_final.InvoiceDate,
		sales_final.title as title,
        sales_cancelled.review_count as review_count, 
        sales_final.total_sale as total_sale, 
        sales_final.Country as Country,
		sum(sales_final.total_sale) over (partition by sales_final.Country) as Total_sales_country
from (sales_final inner join sales_cancelled on sales_final.title = sales_cancelled.title)

-- this method take less time 
use amazon;
select sales_final.InvoiceDate, 
		sales_cancelled.review_count,
		sales_final.total_sale,
        sales_final.Country,
        sum(sales_final.total_sale) over (partition by sales_final.Country) as Total_sales_country

from
(sales_final inner join sales_cancelled on sales_final.title = sales_cancelled.title);

-- Q2:
-- use ecom;
-- SELECT EXTRACT('%d'from sales.InvoiceDate);
SELECT DAY(InvoiceDate)
from sales;

SELECT strftime('%d', InvoiceDate)
from sales;

-- select rows based on condition in one column
use ecom;
SELECT InvoiceNo from sales where InvoiceNo like "C%" ;

-- add new col (with datatype max.value.length)
ALTER TABLE sales
ADD COLUMN InvoiceStatus CHAR (10);
-- DROP InvoiceStatus;
-- ADD COLUMN InvoiceStatus CHAR NOT NULL;

-- update new col
-- disable safe update mode
SET SQL_SAFE_UPDATES=0;
UPDATE `sales` SET `InvoiceStatus` = 'Cancelled' WHERE `InvoiceNo` like "C%";
UPDATE `sales` SET `InvoiceStatus` = 'No_Cancel' WHERE `InvoiceNo` NOT like "C%";
-- enable safe update mode
SET SQL_SAFE_UPDATES=1;

select * from sales;


ALTER TABLE sales 
	ADD COLUMN InvoiceStatus
		CASE InvoiceNo
			WHEN InvoiceNo like "C%" then 'Cancelled'
			ELSE 'Not_cancelled'
		END as InvoiceStatus
    
-- SET InvoiceStatus = 'cancelled' where InvoiceNo like "C%";
-- update [Tablename] set Grade = 'A' where points >90;
-- SET InvoiceDate2 = IF(InvoiceNo like "C%", 'Cancelled', 'Not_cancelled');

-- add a temporary column dependin on values in other column
SELECT InvoiceNo,
CASE WHEN
	InvoiceNo like "C%" then InvoiceDate2 = 'Cancelled'
ELSE 'Not_cancelled'
	END as InvoiceStatus
FROM sales;


ALTER TABLE sales
	ADD COLUMN InvoiceStatus AS
		CASE
		  WHEN (InvoiceNo like "C%") THEN 'Cancelled'
		  ELSE 'Not_cancelled'
		END

--

use ecom;
SELECT sales_final.ASIN as ASIN, sales_cancelled.review_count as review_count
from 
(sales_final inner join sales_cancelled on sales_final.ASIN = sales_cancelled.ASIN)
group by ASIN;


-- how to groupby ‘invoice date (day-wise)’ from sales database and calculate average of total_sale in each day


-- how to add new column ‘cancelled’ based on the ‘InvoiceNo (cancelled items starting with C)’ from sales database and
-- apply two conditional groupby ‘cancelled’ and ‘invoice date (day-wise)’’ 
