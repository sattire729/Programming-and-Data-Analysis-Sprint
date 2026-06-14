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