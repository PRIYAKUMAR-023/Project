use psyliq;

Select * from paytm_epurchase_data;

-- 1)What does the "Category_Grouped" column represent, and how many unique categories are there?

select distinct(category_grouped)
from paytm_epurchase_data
group by category_grouped;

-- 2)Can you list the top 5 shipping cities in terms of the number of orders?

select count(*) as total_orders ,shipping_city
from paytm_epurchase_data
group by shipping_city
order by total_orders desc limit 5;

-- 3)Show me a table with all the data for products that belong to the "Electronics" category.

select * from paytm_epurchase_data 
where category='electronics';

-- 4)Filter the data to show only rows with a "Sale_Flag" of 'Yes'.

select * from paytm_epurchase_data 
where sale_flag='on sale';

-- 5)Sort the data by "Item_Price" in descending order. What is the most expensive item?

select Item_nm,item_price 
from paytm_epurchase_data 
order by item_price desc
limit 1;

-- 6)Apply conditional formatting to highlight all products with a "Special_Price_effective" value below $50 in red.

select * ,case when special_price_effective <50 then'below &50'
          else 'above &50'
	end  as price 
from paytm_epurchase_data 
where color='red';

-- 7)Create a pivot table to find the total sales value for each category.

select sum(item_price),category_grouped from paytm_epurchase_data
group by category_grouped;

-- 8)Create a bar chart to visualize the total sales for each category.

select sum(item_price)as total_sales,category 
from paytm_epurchase_data
group by category 
order by total_sales desc;

-- 9)Create a pie chart to show the distribution of products in the "Family" category.

SELECT Family, COUNT(*) AS total_products
FROM paytm_epurchase_data
GROUP BY Family;


-- 10)Ensure that the "Payment_Method" column only contains valid payment methods (e.g., Visa, MasterCard).
    
update paytm_epurchase_data
set Payment_Method =
    case
        when Payment_Method  not in('visa','mastercard') then null
        else payment_method
    end;
set sql_safe_updates=0;
-- 11)Calculate the average "Quantity" sold for products in the "Clothing" category, grouped by "Product_Gender."

select product_gender,avg(quantity)as avg_quantity from paytm_epurchase_data 
where category='clothing' 
group by product_gender;


-- 12)Find the top 5 products with the highest "Value_CM1" and "Value_CM2" ratios. 

select *,round((value_cm1/value_cm2),2)as ratio
from paytm_epurchase_data
order by ratio desc 
limit 5;

-- 13)Identify the top 3 "Class" categories with the highest total sales. Create a stacked bar chart to represent this data.

select class,sum(item_price)as total_price 
from paytm_epurchase_data
group by class
order by total_price desc
limit 3;


-- 14)Use VLOOKUP or INDEX-MATCH to retrieve the "Color" of a product with a specific "Item_NM."

select Color
from paytm_epurchase_data
where Item_NM = 'your_specific_item_nm';

-- 15)Calculate the total "coupon_money_effective" and "Coupon_Percentage" for products in the "Electronics" category.

select sum(coupon_money_effective),
	   sum(coupon_percentage)
from paytm_epurchase_data
where category='electronics';

-- 16)Perform a time series analysis to identify the month with the highest total sales.

select sum(item_price) as total_price,
	   month(date)as sales_month
from paytm_epurchase_data
group by sales_month
order by total_price desc
limit 1;

-- 17)Calculate the total sales for each "Segment" and create a scatter plot to visualize the relationship between "Item_Price" and "Quantity" in this data.

select segment,sum(item_price)as total_sales from paytm_epurchase_data group by segment;

-- 18)Use the AVERAGEIFS function to find the average "Item_Price" for products that have a "Sale_Flag" of 'Yes.'

select avg(item_price) from paytm_epurchase_data where sale_flag='on sale';

-- 19)Identify products with a "Paid_pr" higher than the average in their respective "Family" and "Brand" groups.

select * from paytm_epurchase_data p where paid_pr>(select avg(paid_pr)as avg_paid from paytm_epurchase_data pe where p.family=pe.family and p.brand=pe.brand);

-- 20)Create a pivot table to show the total sales for each "Color" within the "Clothing" category and use conditional formatting to highlight the highest sales.

select color,sum(item_price)as total_price from paytm_epurchase_data where category='clothing'
group by color;