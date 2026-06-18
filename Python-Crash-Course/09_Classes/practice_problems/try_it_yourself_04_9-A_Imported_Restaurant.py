# 9-10 Imported Restaurant: Using the latest version of restaurant.py from this section, store it in a module named restaurant.py. Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

from restaurant import Restaurant

my_restaurant = Restaurant('Furina Food', 'Furinian')
my_restaurant.describe_restaurant()