# 9-4 Number Served: Start with your program from Exercise 9-1 (page 166). Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again. Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any number you like that could represent how many customers were served in, say, a day of business.

class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value for number served

    def describe_restaurant(self):
        """Print the restaurant name and cuisine type."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        """Set the number of customers served."""
        self.number_served = number

    def increment_number_served(self, additional_customers):
        """Increment the number of customers served."""
        self.number_served += additional_customers

restaurant = Restaurant("Pizza Palace", "Italian")
print(f"{restaurant.restaurant_name} has served {restaurant.number_served} customers.")
restaurant.number_served = 10
print(f"{restaurant.restaurant_name} has served {restaurant.number_served} customers.")

restaurant.set_number_served(25)
print(f"{restaurant.restaurant_name} has served {restaurant.number_served} customers.")

restaurant.increment_number_served(15)
print(f"{restaurant.restaurant_name} has served {restaurant.number_served} customers.")