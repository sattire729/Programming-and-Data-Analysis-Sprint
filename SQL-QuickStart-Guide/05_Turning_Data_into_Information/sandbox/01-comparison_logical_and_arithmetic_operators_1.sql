SELECT
	Total AS [Original Amount],
	Total + 10 AS [Addition Operator],
	Total - 10 AS [Subtraction Operator],
	Total / 10 AS [Division Operator],
	Total * 10 AS [Multiplication Operator],
	Total % 10 AS [Modulo Operator]
FROM
	invoices
ORDER BY
	Total DESC