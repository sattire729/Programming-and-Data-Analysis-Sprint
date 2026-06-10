# 7-4 Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you'll add that topping to their pizza.

prompt = "\nPlease enter the name of the topping you'd like on your pizza"
prompt += ("\nEnter 'quit' when you are finished. ")

active = True
while active:
    topping = input(prompt)
    
    if topping == 'quit':
        active = False
    else:
        print(f"We will add {topping} to your pizza")
        

