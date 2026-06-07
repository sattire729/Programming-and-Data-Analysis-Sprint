# 6-7 People: Start with the program you wrote for Exercise 6-1 (page 102). Make two new dictionaries representing different people, and store all three dictionaries in a list called people.
# Loop through your list of people. As you loop through the list, print everything you know about each person.

information_1 = {'First Name': 'Furina',
    'Last Name': 'de Fontaine',
    'age': '500',
    'city': 'Fontaine'
    }
information_2 = {'First Name': 'Sattire',
    'Last Name': 'Daniel',
    'age': 20,
    'city': 'Haldwani'
    }
information_3 = {'First Name': 'Wey',
    'Last Name': 'Gay',
    'age': 15,
    'city': 'TN'
    }

people = [information_1, information_2, information_3]

for person in people:
    print(f"Full name - {person['First Name']} {person['Last Name']}")
    print(f"Age - {person['age']}")
    print(f"City - {person['city']}\n")
    
