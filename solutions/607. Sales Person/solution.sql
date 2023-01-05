# Write your MySQL query statement below
WITH red_orders AS (
    SELECT
        orders.*
    FROM
        orders
    JOIN
        company
    ON
        orders.com_id = company.com_id
    WHERE
        company.name = 'RED'
)
SELECT
    name
FROM
    SalesPerson
LEFT JOIN
    red_orders
ON
    SalesPerson.sales_id = red_orders.sales_id
WHERE
    red_orders.order_id IS NULL;
