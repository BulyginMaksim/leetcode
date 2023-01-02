# Write your MySQL query statement below
SELECT
    DISTINCT tree_1.id,
    (
        CASE
            WHEN tree_1.p_id IS NULL THEN 'Root'
            WHEN tree_1.p_id IS NOT NULL AND tree_2.id IS NOT NULL THEN 'Inner'
            WHEN tree_1.p_id IS NOT NULL AND tree_2.id IS NULL THEN 'Leaf'
        END
    ) AS type
FROM
    tree AS tree_1
LEFT JOIN
    tree AS tree_2
ON
    tree_1.id = tree_2.p_id;
