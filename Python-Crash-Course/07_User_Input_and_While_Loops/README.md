## Completed Chapter 07 User Input and While Loops  
### Resources and Materials.  
[📄 Click here to open the Annotated PDF](resources_used/07-user-input-and-while-loops-annotations.pdf)
### Key Insights and Progress Log.  

Most programmes are written to solve a user's problem, but to do so, we often need some information from the user that we will work on to give a result, i.e... take user `input` and produce a desired `output`.  
Here we study how we can accept `user input` so our program can then work on it, and to do so we will need the `input()` function.  
We will also learn how to keep programs running as long as users want them to, so they can enter as much information as they need to and then our program can work with all that information, for this we will use Python's `while loop` (will help keep our program keep running as long as certain conditions remain true)
With the ability to work with user input and the ability to control how long our program run, we will be able to write fully interactive programs.  

First we learn `how the input() function works`, it basically pauses our program and waits for the user to enter some text. Once Python recieves the user's input, it assigns that input to a variable to make it convinient for us to work with.  
The `input()` function takes one argument: the `prompt` that we want to display to the use, so they know what kind of information to enter. i.e... the line `<variable_name> = input("<prompt to be shown to user>)` if in a program will display the prompt to the user, then the program will wait till user enters their response and continues after the user presses `ENTER`. The response is assigned to variable <variable_name> and the program continues as normal.  
`Writing clear prompts` everytime we use the `input()` function goes a long way, first we should include a clear, easy-to-follow prompt, second add a space at the end of prompts, it is to seperate the prompt and user's response. we can also assign our prompt to a varibale and pass that variable to the `input()` function, this allows us to build our prompt over several lines, then write a clean input() statement e.g... input(<variable_name>) after assigning the to be displayed prompt to the variable <variable_name> can help us fit a prompt any size without cluttering up the program.  
Random: the operator `+=` takes the data the variable on the left side was assigned to and appends the data to the right side, for numeric data type we get a simple addition and updation of the variable, as for strings, the string provided in the += operator is added to the end of the string the variable was assigned to earlier and the new string is assigned to the variable.  
When we use the input() function, Python interprets everything the user enters as a string, so if someone enters an numerical input, Python will treat it as the string representation of the number, so we won't be able to perform numerical operations, and will get a TypeError if we try to. We can resolve this issue by using the `int()` function, which converts the input string to a numerical value, `<variable> = int(<variable>)` will convert the variable (if have a numerical string) into an int datatype, so we will be able to perform numerical operations on it (the <variable> can hold the input from user) (We should remember that whenever we use numerical input to do calculations and comparisons, we should convert the input value to a numerical representation first).  
A useful tool when working with numerical information is the `modulo operator(%)` which divides one number by another number and return the remainder, e.g... `4 % 3` in python interpreter will return 1, this can be useful to check if a number is divisible by another (0 returned if it is and a nonzero number returned if it isnt), so `m % n == 0` will return True if m is divisible by n and False if it isnt, so it can be used as a nice conditional test in our programs.  
The `for` loop takes a collection of items and executes a block of code once for each item in the collection. In contrast, the `while` loop runs as long as (or while), a certain condition is true.  
The simple `while` loop keeps running the indented block of code following it till the condition associated with it remains true, e.g...
```code
while <conditional test - T/F>:
    <A block of code>

<other code stuff that will run after the while loop is completed>
```
The block of code indented above will keep running again after it reaches its end again and again till the <conditional test - T/F> keeps evaluating to true and will drop out of the while block and move on ahead if and only if the test evaluates to False, this have a logical implication that we need a way for the while loop to stop or we can run into an `infinite while loop`, mostly we have something in the indented block of code that makes the conditonal test false at some point, so that our program doesnt loop forever, (e.g... a variable with an integer value keeps increasing loop thru loop and at one point it makes the while conditional statement false, making the program move on ahead). We have several other ways to manipulate the flow of the program with a while loop, some are specified below:  
`Letting the User Choose When to Quit` `First I` we saw how we can make a program keep running as long as the user wants by putting most of the program in a `while` loop, defining a `quit value` and then keep the program running as long as the user has not entered the quit value. e.g...
```code
prompt = <PROMPT TO SHOW TO THE USER>

<variable_name> = ""
while <variable_name> != '<quit value>':
    <variable_name> = input(prompt)
    <code we want to run for each input user provides via the variable <variable_name>>

print("Thanks for using our program")
```
Here first we defined the <variable_name> as an empty string so Python has something to check the first time it reaches the while loop, since when it first reads the while line and it doesn't have anything to compare to the quit value and will throw an error, so we should make sure to give the variable an initial value, now the program keeps running as long as the user doesnt enter the specific <quit value> we set (we also have to show what is it in the prompt to make sure the user knows how to stop the program, e.g... entering 'quit' and pressing ENTER), when he does, Python jumps out of the while loop and executes the code after the while block, in this case it print the thank you message. The program above is good but it executes the indented block with the variable carrying the quit value too before dropping out of the loop after user enters the quit value (ponder), to have that npt executed we can do a simple edit: 
```code
prompt = <PROMPT TO SHOW TO THE USER>

<variable_name> = ""
while <variable_name> != '<quit value>':
    <variable_name> = input(prompt)

    if message != 'quit'
        <code we want to run for each input user provides via the variable <variable_name>>

print("Thanks for using our program")
```
The entire utility is same but just the upgrade is that the quit value when assigned to the variable is not treated like the actual data from user.
`Second II` we saw how we can upgrade our program from the simple way I explained above and step up our program to be able to work even when there might be several events which could cause the program to stop running, not just one, doing all this in one while statement becomes complicated and difficult so we `use a flag`. For a program that should run only as long as many conditions are true, we can define one variable that determines whether or not the entire program is active. This variable, called a `flag`, acts as a signal to the program. We can write our program so they run while the flag is set to `True` and stop running when any of the several events sets the value of the flag to `False`. As a result, our overall `while` statement needs only one condition; whether the flag is currently True. Then all the other tests can be neatly organised in the rest of the program. A simple code using a flag goes like:
```code
active = True # This is the flag, we associate True so program starts in active state
while active:
    <variable_name> = input(<prompt>)

    if <variable_name> == '<quit_value>':
        active = False #Ponder, we can use such a thing repeatedly for many conditions
    else:
        <a block of code that does smth with the user input>
```
Pros - simpler while statement (since no comparison made in it itself; the logic is taken care of in other parts of the program), also now that we have a flag to indicate whether the overall program is in an active state, it would be easy to add more tests (such as elif statements) for events that should cause the flag variable to become False
`Third III` we then saw how we can exit a loop immediately without running any remaining code in the loop, regardless of the results of any conditional test `using the break statment` (helps direct the flow of our program) we can use it to control which lines of code are executed and which arent, so the program only executes code that we want it to, when we want it to. The simple interactive program using break might go like:
```code
prompt = <smth to display to user, asking for data and providing a quit value>

while True:
    <variable> = input(prompt)

    if <variable> == <quit value>:
        break
    else:
        <"do wtv you want to do with the user data" Block>
```
Now we should notice that a loop that starts with `while True` will run forever unless it reaches a break statement, when it does, Python exits the loop just as it reads `break`. (We can use the break statement in any of Python's loops, eg we could use it to quit a for loop that's working thru a list or a dictionary)
Lastly we see how we `use continue in a loop`, rather than breaking out of a loop entirely without executing the rest of its code, we can use the `continue` statement to return to the beginning of the loop, based on the result of a conditional test, e.g...
```code