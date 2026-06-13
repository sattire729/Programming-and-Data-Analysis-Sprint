/*
CREATED BY: Sattire
CREATED ON: 13/06/26
DESCRIPTION: This query is meant to count the number of customers
whose last names begin with B.
*/

SELECT
	LastName AS 'Last Name'
FROM
	customers
ORDER BY
	LastName ASC
	
-- By observation 4 customers' last name begin with B.