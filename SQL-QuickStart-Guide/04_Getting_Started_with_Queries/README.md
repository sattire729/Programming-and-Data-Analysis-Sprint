## Completed Chapter 03 Exploring a Database in SQLite.  
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
