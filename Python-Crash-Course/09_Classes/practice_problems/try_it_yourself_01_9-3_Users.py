# 9-3 Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user's information. Make another method called greet_user() that prints a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user.

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

# Create several instances representing different users
user1 = User("John", "Doe", 30, "john.doe@example.com")
user2 = User("Jane", "Smith", 25, "jane.smith@example.com")
user3 = User("Bob", "Johnson", 35, "bob.johnson@example.com")

# Call both methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()