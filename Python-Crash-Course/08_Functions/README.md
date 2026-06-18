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

Because a function definition can have multiple parameters, a function call may need multiple arguments. We can pass arguments to our functions in a number of ways, e.g... `positonal arguments` which need to be in the same order the parametres were written, `keyword arguments` where each argument consists of a variable name and a value, and lists and dictionaries of values. we then looked at each of them in turn. 
`Positional Arguments` - When we call a function, Python must match each argument in the function call with a parameter in the function definition. The simplest way to do this is based on the order of the arguments provided. Values matched up this way are called `Positional Arguments`. A simple code might go like: 
```code
def function_name(para1, para2):
    """Whatever the function does"""
    <code which may or may not use the
     2 arguments (to be 100%) provided in the funcion call>

function_name(<arg1>, <arg2>)
```
The definition shows that this function needs 2 arguments (since it has 2 parametres) so we need to provide them both during function call and then we can use them as we like in the function body, simply put, the values <arg1> and "<arg2> will be assigned to variables namesd "para1", "para2" and we can use this variables freely in the function body to do a specific task we like. 
We can also call a function as many times as needed, just changing the arguments while calling the function will act upon the new arguments the same way as it did for every call before them. 
`Order matters in Positional Arguments`, we can get unexpected results if we mix up the order of arguments in a function call when using positional arguments (ponder). Make sure the order of the arguments in your function call matches the order of the parametres in the function's definition. 
`Keyword Arguments` - A keyword argument is a name-value pair that we pass to a function. We directly associate the name and the value within the argument, so when we pass the argument to the function, there s no confusion even if the order is messed up. The code of such function call might go like: 
```code
def function_name(para1, para2):
    """Whatever the function does"""
    <code which may or may not use the
     2 arguments (to be 100%) provided in the funcion call>

function_name(para2=<arg2>, para1=<arg1>)
```
Here the function hasn't changed, but when we call the function, we ecplicitly tell Python which parameter each argument should be matched with, so no worries about matching up order, an equivalent function call would have been `function_name(para1=<arg1>, para2=<arg2>)`.  
When writing a function, we can define a `Default Value` for each paramter. If tan argument for a parameter is provided in the function call, Python uses the argument value, if not then it uses the paramter's default value. Therefore when we set a default value for a parameter in function definition, we can exclude the corresponding argument in function call! The code might go like: 
```code
def function_name(para1, para2=<default arg>):
    """Whatever the function does"""
    <code which may or may not use the
     2 arguments (1st to be 100%, 2nd optional) provided in the funcion call>

function_name(para2=<arg2>, para1=<arg1>)
functon_name(<arg1>, <arg2>)
function_name(<arg1>)
function_name(para1=<arg1>)
```
As logic dictates, the first and second call will have para1 as <arg1> and para2 as <arg2> (Python will ignore the default value if we explicitly provide an arg in function call) but in third and fourth function call, the function will assign <arg1> to para1 and <default arg> to para2! (Note that when we use default values, any parameter with a default value needs to be listed after all the parametres that dont have default values. This allows Python to continue interpreting positional arguments correctly)
Because positional arguments, keyword arguments and default values can all be used together, we will oftn have several equivalent ways to call a function. just like the (1st and 2nd) and (3rd and 4th) function call above. It doesn't really matter which calling style we use. As long as our function call produle the output we want, we should use one which is easiest to understand.  
When we use function we might often face errors about unmatched arguments. `Unmatched Arguments` occur when we provide fewer or more argumnts than a function needs to do its work, if we do provide more or less arguments than prompted i function def, then we get a Error and the traceback gives a TypeError with the location of the problem, and the traceback also tells us by how much did we miss the mark, since it also shows us the parametres names, it shows how using descriptive names for function parametres can come in handy.  

A function doesn't always have to display its outpur directly. Instead, it can process some data and then return a value or set of values. The value the function returns is called a `return value`. The `return statement` takes a value from inside a function and sends it back to the line that called the function. Return value allows us to move much of out program's grunt work into functions, which can simplify the body of our program. The code of such a program can go like: 
```code
def function_name(para1, para2):
    """Whatever the function does"""
    <code which may or may not use the
     2 arguments provided in the funcion call.
     But we create a new variable here with a particular value
     we want to return when the function is called, say return_value>
     return return_value # The return statement with `return` as keyword

variable_name = function_name(<arg1>, <arg 2>)
```
The function function_name takes 2 arguments, assigns it to para1 and para2 named variables and we can then use these to perform an action and assign it to a variable inside function body, e.g... `return_value = f"{para1} and {para2}"` Then in the return statement we set the variable `return_value` to be returned to the callling line of our function. When we call a function that returns a value, we need to provide a variable that the return value can be assigned to (`variable_name` here). Now we can use the returned value as we like!  
Sometimes it makes sense to make an argument optional so that people using the function can choose to provide extra information only if they want to. We can use defaullt values to make an argument optional, e.g... we can assign the paarameter whose value is optional (e.g middle name) an empty default value and ignore the argument unless the user provides a value, we can do so by assigning the optional argument's parameter an empty string ('') in the function def (should be put at the end of all other parametres (ponder)) and then use it in our code only if we recieve an argument by using if statement and the fact that `if <var_name>` returns True if the variable has a value and False when it does not (e.g... is an empty list or even string), so the code might go like: 
```code
def function_name(para1, para2, para3=''):
    """Whatever the function does"""
    if para3:
        <code that considers the fact that we have all 3 arguments
        and assigns the return value to variable `ret`>
    else:
        <code that proceeds without the third optional argument
        and assigns the return value to variable `ret`>
    return ret

result = function_name(<arg1>, <arg2>)
print(result)
result = function_name(<arg1>, <arg2>, <arg3>)
print(result)
```
Here both the function calls work perfectly because we made the 3rd argument optional. (Nice)
Random: We could have assigned `None` instead of an empty string to para3 and could have gotten the same results, `None` is used when a variable has no specific value assigned to it. We can think of it as a placeholder value. In conditional tests, `None` is evaluated to `False`.
A function can return any kind of value we need it o, including more complicated data structures like lists and dictionaries, e.g...
```code
def function_name(para1, para2):
    """Whatever the function does"""
    dict = {'first': para1, 'second': para2}
    return dict

result = function_name(<arg1>, <arg2>)
print(result)
```
and this will print a dictionary as prompted `{'first': <arg1>, 'second': <arg2>}` 
We can use functions with all the Python structures we have learned about so far, e.g... `using a function with a while loop` a simple example goes like:
```code
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me you name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if f_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
```

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

Sometimes we want to accept an arbitiary number of arguments but we dont know ahead of time what kind of information will be passed to the function (therefore using arbitiary positional arguments like above to make a tuple with unknown types of information is no good).  In this case, we write functions that accept as many key-value pairs as the calling statement provides. The code for this goes like: 
```code
def function_name(
    info1, info2, # 2 compulsary regular arguments
    **kwargs # arbitiary number of key-value pairs accepting argument
    )
    """Build a dictionary containing info about any object"""
    kwargs['1st info'] = info1
    kwargs['2nd info'] = info2
    return kwargs

info_dict = function_name('primary info', 'secondary info'
                          3rd info='tertiary information',
                          4th info='quaternary information')
print(info_dict)
```
The definition of function_name expects a first and second information and then it allows the user to pass in as many key-value pairs as they want. The `double asterisks` before the parameter `**kwargs` cause Python to create a dictionary called kwargs containing all the extra key-value pairs the function recieves, within the function, we can access the key-value pairs in kwargs just as we would for any dictionary. 
We then see the the first and second info are to be always recieved in the function definition line, and any more information can be fed by a user in the format: `key=value` and it will be stored in the dictionary named kwargs. During our function call we see that we passed the first and second info and then 2 key-value pairs on top, we assign the returned dictionary to the variable "info_dict" and print `info_dict`:
```code
{'1st info': 'primary information', '2nd info': 'secondary information,
'3rd info': 'tertiary information', '4th info': 'quaternary information'}
```
We can mix positional, keyword, and arbitiary values in many different ways while writing our own function. 
Random: The parameter name `**kwargs` is used often for nonspecific keyword arguments.

Functions already make our code cleaner by seperating blocks of code away from the main program, we can go one step further by storing our functions in a seperate file called a `module` and then `importing` that module into our main program. An `import` statement tells Python to make the code in a module available in the currently running program file. Storing our functions in sepearte files help us hide the details of our program's code and focus on higher level logic, also helping in using same functions across many programs, sharing functions with other programmers etc, knowing how to import functions also allow us to use libriaries of functions that other programmers have written. There are several ways to import a module, as given below:
`1: Importing an Entire Module`: To start importing functions, we first need to create a module. A `module` is a file ending in `.py` that contains the code we want to import into our program. Ofcourse we just make a Python file and put as many functions we want to in it and put the `module` we just created in the same directory as our main program file, to import the entire module to our main program file we use the import statement, e.g... `import module_name` in our program file and voila, Python reads this line and it tells Python to open the file called module_name and capy all the functions from it into our program (it happens BTS just before the program runs, we dont see it). To call a function from an imported module, we enter the name of the module we imported, `module_name`, followed by the name of the functions, `function_name()` seperated by a dot, this code produces the same output as a prpgram that had that function already inside the main program file, again, the syntax for the `import statement` to import an entire module named `module_name.py` is:
```code 
import module_name
``` 
and each function in this module is available through the syntax:
```code
module_name.function_name()
```
`2: Importing Specific Functions`: We can also import a specific function fro a module, the general syntax for this approach is:
```code
from module_name import function_name
```
We can import as many functions as we want from a module by seperating each function's name with a comma:
```code
from module_name import function_1, function_2, function_3
```
With this syntax, we don't need to use the dot notation when we call a function. Because we've explicitly imported the function `function_name` in the import statement, the syntax to use this imported function is now simply:
```code
function_name()
```
`3: Using as to Give a Function an Alias`: If the name of a function we're importing might conflict with an existing name in our program, or if the function name is long, we can use a short, unique `alias` - an alternative name similar to a nickname for the function. We will give the function this special nickname when we import the function, the general syntax for providing an alias is:
```code
from module_name import function_name as fn
```
now we can simply call the imported function function_name by using `fn()` without a dot notations!
`4: Using as to Give a Module an Alias`: We can also provide an alias for a module name. Giving a module a short alias e.g... mn for module_name, allows we to call the module's functions more quickly. Calling mn.function_name() is more conside than calling module_name.function_name() and it lets us keep descriptive name of the function (which is more important) rather than the module, The general syntax of this approach is:
```code
import module_name as mn
```
`5: Importing All Functions in a Module`: We can tell Python to import every function in a module by using the asterisk (*) operator, the general syntax for this approach is:
```code
from module_name import *
```
The asterisk in the import statement tells Python to copy every function from the module module_name into the program file. Becausr every function is imported, we can call each funtion by name without using the dot notation, however this is not the best approach if working with large modules (ponder) The best approach is to import the function or functions we want, or import the entire module and use the dot notation.

`Styling Functions`: Functions should have descriptive names, and these names should use lowecase letters and underscores, module names should follow these conventions as well.
Every function should have a comment that explains consiselt what the function does and it should appear immediately after the function definition and use the docstring format. 
If we specify a default value for a parameter, no spaces should be used on either side of the equal sign.
```code
def function_name(parameter_0, parameter_1='default value')
```
The same convention should be used for keyword arguments in function calls
```code
function_name(value_0, parameter_1='value')
```
PEP 8 recommends to limit lines of code to 79 characters, if a set of parameteres causes a function definition to be longer than 79 character, press ENTER afte the opening parenthesis on the definition line. On the next line, press the TAB key twice to seperate the list of arguments from the body of the function, which should only be indented one level. The structure goes like:
```code
def function_name(
        parameter_0, parameter_1, paramter_2,
        parameter_3, parameter_4):
    function body...