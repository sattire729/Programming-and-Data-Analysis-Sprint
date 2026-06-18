# 9-6 Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.

class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print the restaurant name and cuisine type."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

class IceCreamStand(Restaurant):
    """A simple attempt to model an Ice Cream Stand."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to ice cream stands.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [
            "vanilla", "chocolate", "strawberry", "mint chocolate chip"
            ]
    
    def display_flavors(self):
        """Displays available Ice Cream flavors."""
        print("The flavors available are:")
        for flavor in self.flavors:
            print(f" - {flavor}")

FurinaIce = IceCreamStand('Furina Ice Creams', 'Ice creams')
FurinaIce.display_flavors()