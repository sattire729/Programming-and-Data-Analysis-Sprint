# 6-8 Pets: Make several dictionaries, where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner’s name.
# Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.

pet_1 = {'Kind of Animal': 'Dog',
         'Owner name': 'Sattire',
         'Favorite Food': 'Dog Food'
         }
pet_2 = {'Kind of Animal': 'Hamster',
         'Owner name': 'Wey',
         'Favorite Food': 'Tears'
         }
pet_3 = {'Kind of Animal': 'Cat',
         'Owner name': 'Losercat',
         'Favorite Food': 'Cat Food'
         }
pet_4 = {'Kind of Animal': 'Jet',
         'Owner name': 'Excalibur',
         'Favorite Food': 'Fuel'
         }

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"Kind of Animal - {pet['Kind of Animal']}")
    print(f"Owner name - {pet['Owner name']}")
    print(f"Favorite Food - {pet['Favorite Food']}\n")
