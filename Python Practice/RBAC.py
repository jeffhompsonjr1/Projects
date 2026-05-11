from User_info import Users

class Admin(Users):
    """A class for administrator users"""

    def __init__(self, first, last, middle, age, social, address, city, state, zip_code, phone):
        """Initialize attributes of the parent class"""
        super().__init__(first, last, middle, age, social, address, city, state, zip_code, phone)
        self.privileges = Privileges()

class Privileges(Admin):
    """ This class has one attribute, privilege"""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Display the list of admin privileges"""
        print('Admin privileges:')
        for privilege in self.privileges:
            print(f"- {privilege}")

    

admin_info = Admin('Alice', 'Johnson', 'Marie', 30, '-1111', '7890 Maple Street', 'San Antonio', 'TX', '78201', '210-555-6789')
admin_info.privileges.show_privileges()


        

