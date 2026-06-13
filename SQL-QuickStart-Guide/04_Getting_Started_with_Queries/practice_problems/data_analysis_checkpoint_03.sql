/*
CREATED BY: Sattire
CREATED ON: 13/06/26
DESCRIPTION: This query is meant to help us give the answer to
the 3rd question of Data Analysis Checkpoint of the 4th Ch
*/

SELECT
	FirstName,
	LastName,
	PostalCode
FROM
	customers
ORDER BY
	PostalCode
	
-- There are 4 costomers that do not have a postal code listed