/*
CREATED BY: Sattire
CREATED ON: 13/06/26
DESCRIPTION: This query selects the first 10 
records from the customers table, ordered by 
first name (ascending), then last name 
(descending).
*/

SELECT
	FirstName AS [First Name],
	LastName AS [Last Name],
	Email AS [EMAIL]
FROM
	customers
ORDER By
	FirstName ASC,
	LastName DESC
LIMIT 10