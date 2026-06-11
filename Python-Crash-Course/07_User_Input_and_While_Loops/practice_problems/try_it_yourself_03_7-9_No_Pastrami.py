# 7-9 No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['tuna', 'pastrami','turkey', 'pastrami','ham', 'cheese', 'pastrami']

print("Sorry, we have run out of pastrami today.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("The following sandwiches are still available:")
for sandwich in sandwich_orders:
    print(sandwich.title())