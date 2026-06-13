/*
CREATED BY: Sattire
CREATED ON: 12/06/26
DESCRIPTION: This query selects the first name, 
last name, and email from the customers table, 
ordered by first name
*/

SELECT
	FirstName AS [First Name],
	LastName AS [Last Name],
	Email AS [EMAIL]
FROM
	customers
ORDER BY
	FIrstName ASC,
	LastName DESC