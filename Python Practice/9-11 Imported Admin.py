from RBAC import Admin
""" Import the Admin Class from privilieges file """

administrators_RBAC = Admin("Annie","Williams","N",32,"N/A","3801 Meyers Lane APT 1314","Waco","TX","76705","254-500-8566")

administrators_RBAC.describe_user()

print("\nAnnie Has the following RBAC:")
administrators_RBAC.privileges.show_privileges()

