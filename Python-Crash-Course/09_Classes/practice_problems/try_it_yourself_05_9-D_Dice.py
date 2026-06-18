# 9-13 Dice: Make a class Die with one attribute called sides, which has a default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. Roll each die 10 times.

from random import randint

class Die:
    """A simple attempt to model a die"""

    def __init__(self, sides=6):
        """Initialize attributes for the Die Class."""
        self.sides = sides

    def roll_die(self):
        """Prints a random number between 1 and the number of sides the die has."""
        print(randint(1, self.sides))

print("\nThe results of 6 sided die rolls are:")
die_6 = Die()
for i in range(10):
    die_6.roll_die()

die_10 = Die(10)
die_20 = Die(20)

print("\nThe results of 10 sided die rolls are:")
for i in range(10):
    die_10.roll_die()

print("\nThe results of 20 sided die rolls are:")
for i in range(10):
    die_20.roll_die()