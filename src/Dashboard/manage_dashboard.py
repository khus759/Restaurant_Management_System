
from Src.Authentication.auth_system import AuthSystem
from Src.Dashboard.owner_dashboard import OwnerDashboard
from Src.Dashboard.staff_dashboard import StaffDashboard

def show_dashboard(user_role):
    if user_role == "Owner":
        dashboard = OwnerDashboard()
        dashboard.display_dashboard()
    elif user_role == "Staff":
        dashboard = StaffDashboard()
        dashboard.display_dashboard()
    else:
        print("Invalid role")

def main():
    auth_system = AuthSystem()
    while True:
        print("-"*64)
        print("********* Welcome to the Taste of Tradition Restaurant *********")
        print("-"*64)
        print("1. Signup")
        print("2. Login")
        print("3. Exit")

        try:
            option = input("Choose an option: ")
        except ValueError:
            print("please enter valid input")
            continue

        if option == "1":
            auth_system.signup()
        elif option == "2":
            user = auth_system.login()
            if user:
                show_dashboard(user["role"])
        elif option == "3":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")
