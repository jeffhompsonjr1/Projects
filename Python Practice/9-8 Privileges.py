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

my_info = Users('Jeff', 'Jr.', 'Thompson', 42, '-7777', '3801 Meyers Lane', 'Waco', 'TX', '76710', '254-555-1234')
friend_info = Users('Sally', 'Smith', 'Ann', 35, '-8888', '1234 Main Street', 'Dallas', 'TX', '75201', '214-555-5678')
moms_info = Users('Karen', 'Smith', 'Louise', 65, '-9999', '5678 Oak Avenue', 'Austin', 'TX', '78701', '512-555-9012')
brothers_info = Users('John', 'Smith', 'Michael', 40, '-0000', '9012 Pine Street', 'Houston', 'TX', '77001', '713-555-3456')

my_info.describe_user()
my_info.greet_user()    
print("\n")
friend_info.describe_user()
friend_info.greet_user()
print("\n")
moms_info.describe_user()
moms_info.greet_user()
print("\n")
brothers_info.describe_user()
brothers_info.greet_user()
my_info.increment_login_attempts()
my_info.increment_login_attempts()
my_info.increment_login_attempts()
my_info.reset_login_attempts()
print(f"{my_info.login_attempts}")

class Admin(Users):
    """A class for administrator users"""

    def __init__(self, first, last, middle, age, social, address, city, state, zip_code, phone):
        """Initialize attributes of the parent class"""
        super().__init__(first, last, middle, age, social, address, city, state, zip_code, phone)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Display the list of admin privileges"""
        print('Admin privileges:')
        for privilege in self.privileges:
            print(f"- {privilege}")

admin_info = Admin('Alice', 'Johnson', 'Marie', 30, '-1111', '7890 Maple Street', 'San Antonio', 'TX', '78201', '210-555-6789')
admin_info.show_privileges()

class Privileges(Admin):
    """ This class has one attribute, privilege"""

    def __init__(self, privileges):
        self.privileges = 
        

