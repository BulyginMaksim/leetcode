# Write your MySQL query statement below
WITH salaries_ranked AS (
	SELECT
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS rank_desc
    FROM
        employee
)
SELECT
    MAX(salary) AS SecondHighestSalary
FROM
    salaries_ranked
WHERE
    rank_desc = 2;
