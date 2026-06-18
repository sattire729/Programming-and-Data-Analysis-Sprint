# 9-14 Lottery: Make a list or tuple containing a series of 10 numbers and five letters. Randomly select four numbers or letter from the list and print a message saying that any ticket matching these four numbers and letter wins a prize.

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