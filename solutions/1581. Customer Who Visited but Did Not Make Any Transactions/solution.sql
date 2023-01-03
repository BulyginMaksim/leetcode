# Write your MySQL query statement below
SELECT
    visits.customer_id,
    COUNT(*) AS count_no_trans
FROM
    visits AS visits
LEFT JOIN
    transactions
ON
    visits.visit_id = transactions.visit_id
WHERE
    transactions.visit_id IS NULL
GROUP BY
    visits.customer_id
ORDER BY
    customer_id,
    count_no_trans;
