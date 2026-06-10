# 7-5 Movie Tickets: A movie theater charges different ticket prices depending on a person's age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of the movie ticket.

prompt = "\nPlease enter you age"
prompt += "\n(Enter 'quit' when you are finished.) "

print("Welcome to our Movie Theater!")

while True:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        age = int(age)

    if age < 3:
        print("The ticket for you free of cost")
    elif age >= 3 and age <= 12:
        print("The ticket price for you is $10")
    else:
        print("The ticket price for you is $15")
