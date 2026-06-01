# 6-6 Polling: Use  the code in favorite_languages.py (page 97).
# Make a list of people who should take the favorite languages poll, and include some names that are already in the dictionary and some that are not.
# Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

people = ['larry', 'sarah', 'wey', 'phil', 'michael', 'anna']

for person in people:
    if person in favorite_languages:
        print(f"Thank you for taking the poll, {person.title()}.")
    else:
        print(f"{person.title()}, please take the poll.")
