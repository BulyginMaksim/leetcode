# Write your MySQL query statement below
SELECT
    users.name,
    SUM(amount) AS balance
FROM
    users
JOIN
    transactions
ON
    users.account = transactions.account
GROUP BY
    users.name
HAVING
    SUM(amount) > 10000;
