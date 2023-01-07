# Write your MySQL query statement below
SELECT
    users.user_id as buyer_id,
    users.join_date,
    COALESCE(COUNT(orders.order_id), 0) as orders_in_2019
FROM
    users
LEFT JOIN
    orders
ON
    users.user_id = orders.buyer_id
    AND YEAR(orders.order_date) = 2019
GROUP BY
    users.user_id;
