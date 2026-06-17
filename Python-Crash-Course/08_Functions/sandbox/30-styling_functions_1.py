# If you specify a default value for a parameter, no spaces should be used
# on either side of equal sign, same for keyword arguments in function calls.
function_name(value_0, parameter_1='value')

# Limit lines of code to 79 characters so every line is visible in a reaonably
# sized editor window. If a set of parameters causes a function's definition
# to be longer than 79 characters, press ENTER after the opening parenthesis
# on the def line . On the next line, press the TAB key twice to seperate the
# list of arguments from the body of the function, which will only be indented
# one level
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4):
    function body...

