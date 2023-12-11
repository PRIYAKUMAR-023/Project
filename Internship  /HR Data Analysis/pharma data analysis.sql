show global variables like 'local_infile';
set global local_infile=true;

use psyliq;

-- 1) Retrieve all columns for all records in the dataset.

select * from pharma_analysis;

-- 2)How many unique countries are represented in the dataset?

select distinct(country)from pharma_analysis;

-- 3)Select the names of all the customers on the 'Retail' channel.

select customername 
from pharma_analysis 
where subchannel='Retail';

-- 4)Find the total quantity sold for the ' Antibiotics' product class.

select 
sum(quantity)as total_quantity 
from pharma_analysis 
where productclass='Antibiotics';

-- 5)List all the distinct months present in the dataset.

select 
distinct(month)as month 
from pharma_analysis;

-- 6)Calculate the total sales for each year.

select year,
       sum(sales)as total_sales 
from pharma_analysis
group by year;

-- 7)Find the customer with the highest sales value.

select customername,max(sales)as max_sales from pharma_analysis 
group by customername
order by max_sales desc 
limit 1;

-- 8)Get the names of all employees who are Sales Reps and are managed by 'James Goodwill'.

select distinct(NameofSalesRep) 
from pharma_analysis 
where manager='James goodwill';

-- 9)Retrieve the top 5 cities with the highest sales.

select sum(sales)as total_sales ,city from pharma_analysis
group by city
order by total_sales desc
limit 5;

-- 10)Calculate the average price of products in each sub-channel.

select avg(price)as avg_price,Subchannel 
from pharma_analysis
group by Subchannel;

-- 11)Join the 'Employees' table with the 'Sales' table to get the name of the Sales Rep and the corresponding sales records.



-- 12)Retrieve all sales made by employees from ' Rendsburg ' in the year 2018.

select * from pharma_analysis 
where city='rendsburg' and year=2018;


-- 13)Calculate the total sales for each product class, for each month, and order the results by year, month, and product class.

select sum(sales)as total_sales,year,month,productclass from pharma_analysis
group by productclass,year,month 
order by total_sales;

-- 14)Find the top 3 sales reps with the highest sales in 2019.

select sum(sales)as total_sales,nameofsalesrep from pharma_analysis
where year=2019
group by nameofsalesrep
order by total_sales desc
limit 3;

-- 15)Calculate the monthly total sales for each sub-channel, and then calculate the average monthly sales for each sub-channel over the years.

select Subchannel,month,sum(sales)as total_sales,avg(sales)
from pharma_analysis
group by month,Subchannel;

-- 16)Create a summary report that includes the total sales, average price, and total quantity sold for each product class.

select productclass,sum(sales)as total_sales,avg(price)as avg_price,sum(quantity)as total_quantity 
from pharma_analysis
group by productclass;

-- 17)Find the top 5 customers with the highest sales for each year.

select customername,year,sum(sales)As total_sales from pharma_analysis
group by year,customername
order by year,total_sales desc
limit 5;

-- 18)Calculate the year-over-year growth in sales for each country
SELECT
    current_year.country,
    current_year.year AS current_year,
    current_year.total_sales AS current_year_sales,
    previous_year.year AS previous_year,
    previous_year.total_sales AS previous_year_sales,
    (current_year.total_sales - previous_year.total_sales) / previous_year.total_sales * 100 AS yoy_growth
FROM
    (SELECT country,year,SUM(sales) AS total_sales
        FROM pharma_analysis
        GROUP By country,year) AS current_year
JOIN
    (SELECT country,year,SUM(sales) AS total_sales
        FROM pharma_analysis
        GROUP BY country,year
) AS previous_year
ON
    current_year.country = previous_year.country
    AND current_year.year = previous_year.year + 1
ORDER BY
    current_year.country,
    current_year.year;
    
-- 19)List the months with the lowest sales for each year

SELECT year,month,SUM(sales) AS total_sales
FROM pharma_analysis
GROUP BY year,month
ORDER BY year,total_sales ASC LIMIT 1;

-- 20)Calculate the total sales for each sub-channel in each country, and then find the country with the highest total sales for each sub-channel.

with SubchannelSales AS (
   select
        country,
        subchannel,
        SUM(sales) AS total_sales,
        RANK() OVER (PARTITION BY subchannel ORDER BY SUM(sales) DESC) AS sales_rank
   from
        pharma_analysis
   group by country,subchannel
)
select
    country,
    subchannel,
    total_sales 
from SubchannelSales 
WHERE sales_rank = 1;


