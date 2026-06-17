## Completed Chapter 08 Functions  
### Resources and Materials.  
[📄 Click here to open the Annotated PDF](resources_used/08-functions-annotations.pdf)
### Key Insights and Progress Log.

Here we studied `functions` that are named blocks of code designed to do one specific job. When we want to perform a particular task that we have defined in a function, we `call` the function responsible for it, saves us from typing the same code again and again when we want to do a task multiple times, we just call the function and it tells python to run the code inside the function. We also see that using functions makes our program easier to write, read, test and fix. We will also learn a variety of ways to pass information to functions, we will also learn how to write certain functions whose primary job is to display information and other functions designed to process and return a value or set of values. Finally, we learnt to store functions in seperate files called modules to help organize our main program files.  
 
The simplest structure of a function goes like this:
```code
def function_name(<any information the function needs to run>):
    """<Function Description>"""
    <Code>

function_name()
```
Here in the first line we `defined a function` called function_name(), the `def` keyword informs python that we are defining a function. This is the `function definition`, which tells Python the name of the function and, if applicable, what kinds of information the function needs to do its job. The parenthesis hold that information, here they are empty and the function definition ends in a colon.
Any indented lines that follow the function defition (first line) make up the `function body`. The text on the second line is a comment called a `docstring`, which describes wht the function does, when Python generates documentation for the functions in our programs, it looks for a string immediately after the function's defintion. These strings are usually enclosed in triple quotes, which lets us write multiple lines.
The third line and ahead is the actual code in the body of the function, when we want to use this function, we have to call it. A `function call` tells Python to execute the code in the function (the <code>, we will later know where we get the information we might need in a function). To `call` a function, we write the name of the function, followed by any necessary information in parenthesis.  
