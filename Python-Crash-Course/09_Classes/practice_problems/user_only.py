"""A simple attempt to model a User"""

class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, age, email):
        """Initialize first name, last name, age, and email attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User: {self.first_name} {self.last_name}, Age: {self.age}, Email: {self.email}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back.")
