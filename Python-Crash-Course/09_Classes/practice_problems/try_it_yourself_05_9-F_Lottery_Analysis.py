# 9-15 Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.

from random import choice

numbers = [number for number in range(10)]
letters = ['a', 'r', 'y', 'q', 'o']
pool = numbers + letters

winning_code = []

while len(winning_code) < 4:
    random = choice(pool)
    
    if random not in winning_code:
        winning_code.append(random)

print("Any code with the folloing 4 numbers or letters wins a prize:")
print(winning_code)

lose =[]
win =[]


main_flag = True
while main_flag:
    my_ticket = []
    while len(my_ticket) < 4:
        random = choice(pool)

        if random not in my_ticket:
            my_ticket.append(random)
    
    flag = True
    while flag:
        is_losing_ticket = False
        for character in my_ticket:
            if character not in winning_code:
                is_losing_ticket = True
                break
        
        if is_losing_ticket:
            lose.append(my_ticket)
            print(my_ticket)
        else:
            main_flag = False

        flag = False


win.append(my_ticket)
print(len(lose))
print(win)

