# 8-12 Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that's being ordered. Call the function three times, using a different number of arguments each time.

def build_sandwich(*items):
    """"""
    print("\nMaking the Sandwich:")
    for item in items:
        print(f'{item.title()} is being added to your sandwich')

    print("The sandwich is ready!")

build_sandwich('Potato', 'ham', 'Lettuce', 'Tomato')
build_sandwich('Lettuce', 'Tomato', 'onion')
build_sandwich('chicken', 'tomato', 'pickle', 'lettuce', 'oregano')