SELECT
	Total AS [Original Amount],
	Total * 1.15 AS [Taxed amount (15%)]
FROM
	invoices
ORDER BY
	Total DESC