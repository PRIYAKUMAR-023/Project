create database psyliq;
use psyliq;

select * from general_data;
select * from employee_survey_data;
select * from manager_survey_data;

-- 1)Retrieve the total number of employees in the dataset.

select count(Emp_Name)as Total_employee from general_data;

-- 2)List all unique job roles in the dataset.

select 
distinct(jobrole) as unique_role
from general_data;

-- 3)Find the average age of employees.

select 
avg(age)as avg_age 
from general_data;

-- 4)Retrieve the names and ages of employees who have worked at the company for more than 5 years.

select 
Emp_name,age 
from general_data
where TotalWorkingYears>5;

-- 5)Get a count of employees grouped by their department.

select 
department,count(employeeid) as employee_count 
from general_data 
group by department;

-- 6)List employees who have 'High' Job Satisfaction.

select
g.Emp_Name 
from general_data as g
inner join employee_survey_data as e 
on e.employeeid=g.employeeid
where jobsatisfaction =(select max(jobsatisfaction)from employee_survey_data);

-- 7)Find the highest Monthly Income in the dataset.

select 
max(MonthlyIncome)as max_income 
from general_data;

-- 8)List employees who have 'Travel_Rarely' as their BusinessTravel type.

select 
Emp_Name 
from general_data 
where Business_travel='Travel_Rarely';

-- 9)Retrieve the distinct MaritalStatus categories in the dataset.

select distinct(maritalStatus)from general_data;

-- 10)Get a list of employees with more than 2 years of work experience but less than 4 years in their current role.

select Emp_name 
from general_data 
where yearswithcurrmanager>2 and yearswithcurrmanager<4;

-- 11)List employees who have changed their job roles within the company (JobLevel and JobRole differ from their previous job).
select employeeid,Emp_name,current_level,current_role,previousjoblevel,previousjobrole from (
	select employeeid,
			emp_name,
            joblevel as current_level,
            jobrole as current_role,
            lag(jobrole)over(partition by employeeid order by yearsatcompany)as previousjobrole,
            lag(joblevel)over(partition by employeeid order by yearsatcompany)as previousjoblevel
	from general_data) as changed_jobs
where (current_level<> previousjoblevel) or (current_role <> previousjobrole);

-- 12)Find the average distance from home for employees in each department.

select department, Avg(distinct distance_from_home)
 from general_data group by department;

-- 13)Retrieve the top 5 employees with the highest MonthlyIncome.

select emp_name,monthlyincome 
from general_data
order by monthlyincome desc limit 5;

-- 14)Calculate the percentage of employees who have had a promotion in the last year.

with countofpromotion as (select  count(*) AS promotion_people 
FROM general_data WHERE yearssincelastpromotion <> 0)
SELECT 
(promotion_people / (SELECT COUNT(*) FROM general_data)) * 100 
AS percentage_of_promotion
FROM countofpromotion;

-- 15)List the employees with the highest and lowest EnvironmentSatisfaction.

select g.employeeid,g.emp_name,esd.environmentsatisfaction 
from general_data as g inner join employee_survey_data as esd 
on esd.employeeid=g.employeeid
where environmentsatisfaction in ((select max(environmentsatisfaction) from employee_survey_data) 
union (select min(environmentsatisfaction)from employee_survey_data));

-- 16)Find the employees who have the same JobRole and MaritalStatus.

select JobRole,MaritalStatus,count(*) AS NumEmployees
from general_data 
group by  JobRole, MaritalStatus 
having count(*) > 1;

-- 17)List the employees with the highest TotalWorkingYears who also have a PerformanceRating of 4.

select g.employeeid,g.emp_name from general_data as g 
inner join manager_survey_data as msd 
on msd.employeeid=g.employeeid 
where performancerating=4 and 
(select max(totalworkingyears)from general_data);

-- 18) Calculate the average Age and JobSatisfaction for each BusinessTravel type.

select business_travel,
avg(g.age)as avg_age,
avg(esd.jobsatisfaction)as avg_jobsatisfaction from general_data as g 
inner join employee_survey_data as esd
on esd.employeeid=g.employeeid group by business_travel;


-- 19)Retrieve the most common EducationField among employees.

select education_field,
	   count(*) as Numofemployees
from general_data 
group by education_field
order by Numofemployees desc
limit 1;

-- 20)List the employees who have worked for the company the longest but haven't had a promotion.

select Employeeid,emp_name from general_data 
where yearssincelastpromotion=0 and
(select max(yearsatcompany) from general_data);

