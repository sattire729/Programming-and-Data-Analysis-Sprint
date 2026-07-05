## Completed Chapter 04 Getting Started with Queries. 
### Resources and Materials.  
[📄 Click here to open the Annotated PDF](resources_used/04-getting-started-with-queries-annotations.pdf)
### Key Insights and Progress Log.  
We started with some common easy-to-use commands in this chapter, also the basics of writing a good query and formatting the results, so that we will be able to select individual fields from specific database and display those fields in alphabetical order.  
First is `adding comments to queries`, `comments` are plain english sentences used to help add insight and authoring information about SQL statements that we create (industry best practice btw, ponder why its so  nice). There are 2 ways to create a comment - Preceding anything written in the Query Pane with 2 hyphens `(--)` creates a comment on the line. A `comment block` is a multi line comment, it's created using the font slash and star symbol to open the block `/*`, followed by a star and a front slash `*/`, which closes the block, anything that falls between the opening and closing symbols becomes part of the comment. e.g...
```code
--This is a line of comment
/*
CREATED BY: <Name or smth>
CREATED ON: <Date or smth>
DESCRIPTION: <What your query does consisely>
*/
<Your Query>

Then we understood `The Structure of a Basic Query`, writing a query is like asking a question in any natural language, the phrasing matters, the details matter, and the order of the words matter. In the creating of an SQL query, we need to consider the following 5 questions:
```code
1 .What database are we speaking to?
2. What table within that database are we requesting the data FROM?
3. What fields within the table are we intersted in? / What fields within the table are we SELECTing to display?
4. Do we want to exclude any data, filter or omit any range or time period?
5. In one concise sentence, what does our query do?
```
The purpose of the foregoing question is to help us build a bridge between the natural language we use everyday and the language of SQL.  

Next came `Starting to write our query`, where we wrote our first sql query, we noticed that we can use the existing Execute SQL tab labeled 'SQL 1" or start a new Query Pane tab, in the same way that we would open a new web browser tab, by clicking on the `Open Tab Button`. With our new Query Pane opened, the first thing we write is a comment block: 
```code
/*
CREATED BY: <Name or smth>
CREATED ON: <Date or smth>
DESCRIPTION: <What your query does consisely>
*/
```
The query will come after this, for example, if we want to know in sTunes the complete list of first names, last names, and customer email address from the database, we can curate a query by asking the question mentioned above:
```code
1 - Here we only have one database rn - sTunes Database (open it in the DB Browser)  
2 - The most promising table we see when we browse our database is the "customers" table
3 - We can see this from the Browse Data tab. if we click on that tab and select the costomers table in our drop-down menu, we see that is has fields for the first name, last name, and email.  
4 - We dont want to omit anything for now
5 - This query will select the first name, last name and email address from the customers table
```
After adding the comment block, we start by typing `FROM customers`, this tells our query what table to look in for its data. Then type the keyword `SELECT` above the `FROM` clause, followed by the names of the fields within the `customers` table that we wish to view. Each field name is seperated by a comma. The comma tells SQL to expect another fiels. The code looks like:
```code
/*
CREATED BY: Sattire
CREATED ON: DD/MM/YY
DESCRIPTION: This query selects the first name, last name, and email from the customers table.
*/

SELECT
    FirstName,
    LastName,
    Email
FROM
    customers;
```
We can run the statement by clicking on the `Execute SQL play button` in the `menu bar`. The results are displayed in the `Results Pane` below (The requested fields from the specified table), the `MessagesPane` also shows information about the query (How many rows returned, the time taken and the Query itself too!).  

All queries must conform to a certain syntax (`coding syntax`) to be understood by SQL browser, but there is more than just that, it is also important that other database users can understand and follow our queries, the practice of writing queries in a standardized, readable, and consistent way is knows as `coding convention`.  
First we understood that the special symbol (*) tells the SQL browser to retrieve and display all fields in a table, so a `*` symbol after `SELECT` will select all fields.  
The semicolon at the end of the statement is optional in this case, since we are only writing one SQL statement. The semicolon denotes the end of an SQL statement.  
In the `SELECT` clause, we have chosen 3 fields to display. We must seperate every field with a comma (except for the last field). Omitting a comma between fields or adding a comma after the last field are both common syntax mistakes that will result in a `syntax error` appearing in our query in our Results Pane.  
We could write the entire query on one single line instead of breaking in into multiple lines like done above and the SQL browser would still recognise the code and return results.  But its best practice to seperate queries into clauses with the content of each clause indented on a new line. 

If we apply an `alias` to a field name in our query, then the name of a field in our results pane can be edited for our convienience. An alias is always listedd directly after the name of a field from our database. Aliases are commonly associated with the `AS` keyword, however, the use of the `AS` keyword between field name and the alias name is optional in most RDBMS impementations. Note that we can create an alias by just writing `<orig> AS <alias>` or `<orig> <alias>` if the alias contains only one word and we have to close the multi word aliases in some sort of demarcation, either single quotes ('') or square brackets [] in the case below otherwise the same sytax as above. 
```code
/*
CREATED BY: Sattire
CREATED ON: DD/MM/YY
DESCRIPTION: This query selects the first name, last name, email and phone number fields from the customers table and demonstrates 4 different ways to create an alias.
*/

SELECT
    FirstName AS 'First Name',
    LastName AS [Last Name],
    Email AS EMAIL
    Phone CELL
FROM
    customers
```
Adding alias will not change the data in the database. Aliases only alter how fields are displayed in the Results Pane.  

The `ORDER BY` clause (after the `FROM` clause) allows us to sort our query results by any field(s) we choose.The default sort order is ascending (A-Z). The special keyword `ASC`, which specifies ascending order, is optional. To sort in decreasing order (Z-A), we would add the keyword DESC after the field being sorted. `ORDER BY` LastName `DESC` would sort the aliased column Last Name in descending order.  
```code
/*
CREATED BY: Sattire
CREATED ON: DD/MM/YY
DESCRIPTION: This query selects the first name, last name, and emai from the customers table, ordered by Last Name
*/

SELECT
    FirstName AS 'First Name',
    LastName AS [Last Name],
    Email AS EMAIL
    
FROM
    customers
ORDER BY
    LastName ASC
```
We can use the `ORDER BY` clause to sort by multiple columns as well, here we will sory first by First Name (ascending) and then by Last Name (Desc) (First has more priority and the next ones are tiebreakers). This weill require us to list the 2 fields in our `ORDER BY` clause. Just like the `SELECT` clause, when listing multiple fields we must seperate them by commas.
```code
/*
CREATED BY: Sattire
CREATED ON: DD/MM/YY
DESCRIPTION: This query selects the first name, last name, and emai from the customers table, ordered by first name (ascending), then last name (descending)
*/

SELECT
    FirstName AS 'First Name',
    LastName AS [Last Name],
    Email AS [EMAIL]
FROM
    customers
ORDER BY
    FirstName ASC,
    LastName DESC
```

Sometimes we are not interested in all the records in the fields, if that is the case, then we can limit our results to a specified number of rows by the keyword `LIMIT`. Adding the keyword `LIMIT 10` after the `ORDER BY` clause returns only the first ten records from the query in the sort order we specify (ponder the result of using the `LIMIT` keyword before the `ORDER BY` clause vs reversing this order)
```code
/*
CREATED BY: Sattire
CREATED ON: DD/MM/YY
DESCRIPTION: This query selects the first 10 records from the customers table, ordered by first name (ascending), then last name (descending).
*/

SELECT
    FirstName AS 'First Name',
    LastName AS [Last Name],
    Email AS [EMAIL]
FROM
    customers
ORDER BY
    FirstName ASC,
    LastName DESC
LIMIT 10
```
Note that this query performs `ORDER BY` operation first and then applied the limit, so we get the rows that comes in top 10 in ascending order of First name then descending order of Last name, the opposite order will have a different result.
