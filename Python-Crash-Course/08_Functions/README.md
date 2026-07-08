## Completed Chapter 08 Functions  
### Resources and Materials.  
[📄 Click here to open the Annotated PDF](resources_used/08-functions-annotations.pdf)
### Key Insights and Progress Log.

Here we studied `functions` that are named blocks of code designed to do one specific job. When we want to perform a particular task that we have defined in a function, we `call` the function responsible for it, saves us from typing the same code again and again when we want to do a task multiple times, we just call the function and it tells python to run the code inside the function. We also see that using functions makes our program easier to write, read, test and fix. We will also learn a variety of ways to pass information to functions, we will also learn how to write certain functions whose primary job is to display information and other functions designed to process and return a value or set of values. Finally, we learnt to store functions in seperate files called modules to help organize our main program files.  
 
The simplest structure of a function goes like this:
```code
def function_name():
    """<Function Description>"""
    <Code>

function_name()
```
Here in the first line we `defined a function` called function_name(), the `def` keyword informs python that we are defining a function. This is the `function definition`, which tells Python the name of the function and, if applicable, what kinds of information the function needs to do its job. The parenthesis hold that information, here they are empty and the function definition ends in a colon.
Any indented lines that follow the function defition (first line) make up the `function body`. The text on the second line is a comment called a `docstring`, which describes wht the function does, when Python generates documentation for the functions in our programs, it looks for a string immediately after the function's defintion. These strings are usually enclosed in triple quotes, which lets us write multiple lines.
The third line and ahead is the actual code in the body of the function, when we want to use this function, we have to call it. A `function call` tells Python to execute the code in the function (the </code>, we will later know where we get the information we might need in a function). To `call` a function, we write the name of the function, followed by any necessary information in parenthesis (done in final line above)
We can `pass information to a function` easily, e.g... in the above code say we put a variable name inside the parenthesis of function in the function definition, then it would allow the function to accept any value of the variable we specify and we can use it in the </code> part in function body. The function will now expect us to provide a value of that variable everytime we call it, e.g...
```code
def function_name(var):
    """<Function Description>"""
    <Code>

function_name(val)
```
here the code will pass the value "val" to the variable "var" at the time we call it and we can use this variable any way we like in </code>.  
The variable "var" in the defintion of function_name above is an example of a `parameter`, a piece of information the function needs to do its job. The value "val" in the function call is an `argument`. An `argument` is a piece of information that's passed from a function call to a function. When we call the function, we place the value we want the function to work with in the parentheses. 

We can pass a list to a function when needed (or even more complex objects like dictionaries), when we do, the function gets direct access to the contents of the list. One simple example of `Passing a List` to a function might go like:
```code
def function_name(<[parameter] variable containing list>):
    """<Function Description>"""
    <code where we can use the provided list in any way, e.g... for loop>

function_name(<[argument] variable containing list>)
```
When we pass a list to a function. the function can modify the list. Any changes made to the list inside the function's body are permanent, allowing us to work efficiently even when we're dealing with large amounts of data, e.g... we can move items from one list to another empty one using functions (could have done without functions too, ponder the benefits of using (different) functions for each specific job over simple code). The code might go like
```code
def move_items(full_list, empty_list):
    """
    Simulate moving each item, until none are left.
    Move each item from full_list to empty_list
    """
    while full_list:
        current_item = full_list.pop()
        print(f"Moving item: {current_item})
        empty_list.append(current_item)

def show_final_results(full_list, empty_list):
    print("This is the list full_list: ")
    print(full_list)
    print("\nThis is the list empty_list")
    for item in empty_list:
        print(item)
```
We have defined the function move_items() with 2 parametres and it will take 2 lists as the arguments in function call like `move_items(list_1, list_2)` and will move all items from list_1 to list_2, then we defined the function show_final_results() which will print both the lists (which have to be provided in function call), this is very organised way to carry on this specific task, the code that does most of the work has been moved to two seperate functions, which makes the main part of the program easier to understand. The main body can just go like:
```code
list_1 = [item1, item2, item3, item 4]
list_2 = []

move_items(list_1, list_2)
show_final_results(list_1, list_2)
```
This is better since if further in our code if we want to do the same operation again but to different list, we can just pass them as  arguments to our already defined functions, and if we want to modify the function we defined in some way, we can just do it once and the changes will take place everywhere the function was called. This also shows how every function should have one specific job, if we write a function and notice the function is doing many differnt tasks, we can split the code into 2 functions. 
Sometimes we want to `prevent a function from modifying a list`. We can do so easily by passing the function a copy of the list, not the original so that the original list stays unaffected, e.g... while calling the function move_items above we can use `move_items(list_1[:], list_2)`, here the slice notation [:] makes a copy of the list to send to the function. So basically the blueprint of sending a copt of a list to a function goes like:
```code
function_name(list_name[:])
```
Also we should note that even though we can preserve the contents of a list by passing a copy of it to our functions, we should pass the original list unless we have specific reason to pass a copy. Its more efficient for a function to work with an existing list, because it avoids using he time and memory needed to make a seperate list.  

Sometimes we wont know ahead of time how many arguments a function needs to accept, fortunately Python allows a function to collect an arbitiary number of arguments from the calling statement. a parameter in format `*<parameter_name>` acceots as many arguments as the calling line provides. The asterisk in the parameter name tells Python to make a `tuple` called <parameter_name>, containing all the value the function revieves, note that now, during the function call, Python packs the arguments into a tuple even if the function recieves only one value. The code might go like:
```code
def function_name(*<parameter_name>):
    """Print the argements provided"""
    print(<parameter_name>)

function_name(item1)
function_name(item1, item2, item3)
```
The results will be:
```code
(item1,)
(item1, item2, item3)
```
Note that we could also have looped thru the typle named <parameter_name> in the function body. This syntax works no matter how many arguments the function recieves.  
If we want a function to accept several different kinds of arguments, the parameter that accepts an arbitiary number of arguments must be placed last in the function definition. Python matches `positional` and `keyword` arguments first and then collects any remaining arguments in the final parameter, e.g...
```code
def function_name(noun, *adjs):
    """
    Print the arguments provided, first argument as a noun and 2nd parameter as its adjectives
    """
    print(f"\nThe noun {noun} is: ")
    for adj in adjs:
        print(f"- {adj}")

function_name('cat', 'agile')
function_name('cow', 'fat', 'milky', 'heavy')
```
Ad logic dictates, here in the function definition, Python assigns the first value it recieves to the parameter `noun`, all other values that come after are stored in the tuple `adjs` , so ofcourse the result is:
```code

The noun cat is: 
- agile

The noun cow is:
- fat
- milky
- heavy
```
Random note: We will often see the generic parameter name `*args` which collects `arbitiary positional arguments` like this.

