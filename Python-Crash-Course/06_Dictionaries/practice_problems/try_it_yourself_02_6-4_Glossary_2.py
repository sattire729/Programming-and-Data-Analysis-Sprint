# 6-4 Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-2 by replacing your series of print() calls with a loop that runs through dictionary's keys and values. 
# Where you're sure your loop works, add five more python terms to your glossary.
# When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {'print()': 'displays the value in terminal',
    'upper()': 'method that returns the value of a string as all uppercase',
    'pop()': 'method that deletes the last value in a list and lets us use it',
    'if': 'keyword that runs the indented code just below it if it has True and ignores if it has Falsee',
    'python': 'A programming language',
    'set': 'an unordered collection ofr objects, with no repetition',
    'items()': 'method that returns all key value pairs of a dictionary',
    'values()': 'method that returns all values from a dictionary',
    'keys()': 'method that returns all keys from a dictionary',
    'get()': 'method that returns the value of a key if it exists in a dictionary and returns None if it does not exist in a dictionary',
    }

for key, value in glossary.items():
    print(f"\n{key}\n{value}")