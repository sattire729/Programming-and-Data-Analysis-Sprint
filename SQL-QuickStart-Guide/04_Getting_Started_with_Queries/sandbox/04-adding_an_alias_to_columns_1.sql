/*
CREATED BY: Sattire
CREATED ON: 12/06/26
DESCRIPTION: This query selects the first name, 
last name, email, and phone number fields from 
the customers table and demonstrates four 
different ways to create an alias. 
*/

SELECT
	FirstName AS 'First Name',
	LastName AS [Last Name],
	Email AS EMAIL,
	Phone CELL
FROM
	customers