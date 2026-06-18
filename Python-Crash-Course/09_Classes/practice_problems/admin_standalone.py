"""A simple attempt to model an Admin"""

from user_only import User

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