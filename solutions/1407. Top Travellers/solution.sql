# Write your MySQL query statement below
SELECT
    users.name AS name,
    SUM(COALESCE(rides.distance, 0)) AS travelled_distance
FROM
    users
LEFT JOIN
    rides
ON
    rides.user_id = users.id
GROUP BY
    users.id
ORDER BY
    travelled_distance DESC,
    name;
