class Users:
    """Initialize a class to store user information"""

    def __init__(self, first, last, middle, age, social, address, city, state, zip_code, phone):
        """Initialize attributes to store user information"""
        self.first_name = first
        self.last_name = last
        self.middle_name = middle
        self.age = age
        self.social_security = social
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information"""
        print(f"User's name: {self.first_name} {self.middle_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Social Security Number: {self.social_security}")
        print(f"Address: {self.address}, {self.city}, {self.state} {self.zip_code}")
        print(f"Phone number: {self.phone}")

    def greet_user(self):
        """Print a personalized greeting to the user"""
        print(f"Hello, {self.first_name}! Welcome back!")

    def increment_login_attempts(self):
        """ Increment the number of login attempts by 1."""
        self.login_attempts += 1
        print(f"Login attempts: {self.login_attempts}")

    def reset_login_attempts(self):
        """Reset the number of login attempts to 0."""
        self.login_attempts = 0
