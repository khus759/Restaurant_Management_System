from Src.Authentication.auth_system import AuthSystem
from Src.Menu_management.menu_feature import MenuManagement

def main():
    auth_system = AuthSystem()
    menu_management = MenuManagement()

    while True:
        print("\n********* Welcome to the Restaurant Management System **********")
        print("1. Signup")
        print("2. Login")
        print("3. Exit")

        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 3.")
            continue

        if option == 1:
            auth_system.signup()
        elif option == 2:
            current_user = auth_system.login()
            if current_user:  # Only proceed if login is successful
                while True:
                    print("\n********* Menu Management *********")
                    print("1. Show Menu")
                    print("2. Add Menu Item")
                    print("3. Update Menu Item")
                    print("4. Delete Menu Item")
                    print("5. Logout")

                    try:
                        action = int(input("Choose an action: "))
                    except ValueError:
                        print("Invalid input! Please enter a number between 1 and 5.")
                        continue

                    if action == 1:
                        menu_management.show_menu()
                    elif action == 2:
                        menu_management.add_menu_item()
                    elif action == 3:
                        menu_management.update_menu_item()
                    elif action == 4:
                        menu_management.delete_menu_item()
                    elif action == 5:
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif option == 3:
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option! Please choose again.")

# Run the main function only if the script is executed directly
# if __name__ == "__main__":
#     main()
