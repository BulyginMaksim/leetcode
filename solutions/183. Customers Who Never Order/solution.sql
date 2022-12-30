/* Write your PL/SQL query statement below */
SELECT
    c.name AS customers
FROM
    Customers AS c
LEFT JOIN
    Orders AS o
ON
    o.customerId = c.Id
WHERE
    o.customerId IS NULL;
