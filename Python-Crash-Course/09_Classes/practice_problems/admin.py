"""A simple attempt to model a user, an admin, and privileges."""

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

class Privileges:
    """A simple attempt to model the privileges of an Admin."""

    def __init__(self):
        """Initialized privileges attributes."""
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        """Lists admin's set of privileges."""
        print("The admin has following perms:")
        for privilege in self.privileges:
            print(f" - {privilege}")

class Admin(User):
    """A simple attempt to model an admin."""

    def __init__(self, first_name, last_name, age, email):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to Admins.
        """
        super().__init__(first_name, last_name, age, email)
        self.privileges = Privileges()