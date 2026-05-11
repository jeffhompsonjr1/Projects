import RBAC, User_info

""" Import the Admin Class from privilieges file """

new_user = RBAC.Admin("Jeff", "Thompson", "-",42, "592-22-6838", "3801 Meyers Lane APT 1314", "Waco","TX","76705", "870-718-0782")

new_admin = new_user.privileges.show_privileges()

print(new_admin)
