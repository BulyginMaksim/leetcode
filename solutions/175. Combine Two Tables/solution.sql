# Write your MySQL query statement below
SELECT
    person.firstName,
    person.lastName,
    address.city,
    address.state
FROM
    person AS person
LEFT JOIN
    address AS address
ON
    person.personId = address.personId;
