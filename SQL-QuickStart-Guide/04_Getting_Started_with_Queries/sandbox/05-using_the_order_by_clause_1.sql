/*
CREATED BY: Sattire
CREATED ON: 12/06/26
DESCRIPTION: This query selects the first name, 
last name, and email from the customers table, 
ordered by Last Name.
*/

SELECT
	FirstName AS 'First Name',
	LastName AS [Last Name],
	Email EMAIL
FROM
	customers
ORDER BY
	LastName ASC