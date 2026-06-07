# 6-10 Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

favorite_numbers = {'Sattire': [7, 3, 9],
    'Wey': [6, 7],
    'Losercat': [13, 17],
    'larper': [2, 4, 11],
    'tsoi': [6, 9, 27],
    }

for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s Favorite Numbers are:")
    for number in numbers:
        print(f"\t{number}")