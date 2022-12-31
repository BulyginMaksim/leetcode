/* Write your PL/SQL query statement below */
UPDATE
    salary
SET sex  = (
    CASE
        WHEN sex = 'm'
        THEN 'f'
        ELSE 'm'
    END
);
