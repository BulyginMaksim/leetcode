# Write your MySQL query statement below
SELECT
    product.product_id,
    product.product_name
FROM
    sales
JOIN
    product
ON
    sales.product_id = product.product_id
GROUP BY
    product.product_id,
    product.product_name
HAVING
    MIN(sales.sale_date) >= CAST('2019-01-01' AS DATE)
    AND MAX(sales.sale_date) <= CAST('2019-03-31' AS DATE)
