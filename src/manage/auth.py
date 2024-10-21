
from src.authentication.auth_system import AuthSystem

def run_auth_system():
    auth_system = AuthSystem()

    def display_menu():
        print("\n1. Signup")
        print("2. Login")
        print("3. Exit")

    while True:
        display_menu()

        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 3.")
            continue

        if option == 1:
            auth_system.signup()
        elif option == 2:
            auth_system.login()
        elif option == 3:
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option! Please choose again.")
