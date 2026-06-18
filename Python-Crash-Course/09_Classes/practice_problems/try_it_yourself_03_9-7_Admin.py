# 9-7 Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 166) or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator's set of privileges. Create an instance of Admin, and call your method.

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

class Admin(User):
    """A simple attempt to model an admin."""

    def __init__(self, first_name, last_name, age, email):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to Admins.
        """
        super().__init__(first_name, last_name, age, email)
        self.privileges = [
            "can add post", "can delete post", "can ban user"
            ]
        
    def show_privileges(self):
        """Lists admin's set of privileges."""
        print("The admin has following perms:")
        for privilege in self.privileges:
            print(f" - {privilege}")

sattire = Admin('Sattire', 729, 20, 'cuttingbudgets@gmail.com')
sattire.show_privileges()   