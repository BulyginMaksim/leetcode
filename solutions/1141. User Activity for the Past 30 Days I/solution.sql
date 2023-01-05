# Write your MySQL query statement below
SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM
    activity
WHERE
    activity_date <= STR_TO_DATE('2019-07-27', '%Y-%m-%d')
    AND activity_date > DATE_SUB(STR_TO_DATE('2019-07-27', '%Y-%m-%d'), INTERVAL 30 DAY)
GROUP BY
    activity_date;
