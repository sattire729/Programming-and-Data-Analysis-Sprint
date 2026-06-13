/*
CREATED BY: Sattire
CREATED ON: 12/06/26
DESCRIPTION: This query selects the first name, 
last name, and email from the customers table, 
ordered by first name
*/

SELECT
	LastName AS [Last Name],	
	FirstName AS [First Name],
	Email AS [EMAIL]
FROM
	customers
ORDER BY
	LastName ASC