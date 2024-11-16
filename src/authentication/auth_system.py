import uuid
import maskpass  # Secure password input
from Src.Authentication.file_operation import load_users, save_users
from Src.Utility.validation import (
    validate_name, validate_email, validate_password,
    validate_phone_number, validate_date_of_birth
)
from Src.Utility.user_input import get_valid_input
from Src.Utility.path_manager import users_file
from Src.Messages.authentication import AuthHandler
from Src.Utility.color import Colors

class AuthSystem:
    def __init__(self):
        self.users_file = users_file
        self.current_user = None
        self.message_handler = AuthHandler()
        self.color = Colors()

    def signup(self):
        users = load_users(self.users_file)

        while True:
            name = get_valid_input(f"{Colors.CYAN}Enter your name: ", validate_name)

            
            while True:
                email = get_valid_input("Enter your email: ", validate_email).lower()
                if any(user['email'] == email for user in users):
                    print("This email ID is already taken. Please try a different email.")
                else:
                    break

            
            while True:
                password = maskpass.askpass("Enter a password (6+ characters): ", mask="*")
                if validate_password(password):
                    break
                print("Invalid password. Please try again.")

            phone = get_valid_input("Enter your phone number (10 digits): ", validate_phone_number)
            dob = get_valid_input("Enter your date of birth (YYYY-MM-DD): ", validate_date_of_birth)

            # Automatically assign roles
            owner_count = sum(1 for user in users if user['role'].upper() == 'OWNER')
            if owner_count == 0:
                role = "Owner"  # First user becomes the owner
            else:
                role = "Staff"  # All subsequent users become staff

            # Generate a unique user ID
            user_id = str(uuid.uuid4()).replace("-", "")[:8].upper()

            # Create new user object
            new_user = {
                'id': user_id,
                'name': name,
                'email': email,
                'password': password,
                'phone': phone,
                'role': role,
                'date_of_birth': dob
            }

            users.append(new_user)
            save_users(self.users_file, users)

            self.message_handler.signup_successful()
            break

    def login(self):
        users = load_users(self.users_file)
        while True:
            email = get_valid_input("Enter your email: ", validate_email).lower()

            password = maskpass.askpass(f"{Colors.RESET}Enter your password: ", mask="*")

            user = next((user for user in users if user['email'] == email and user['password'] == password), None)
            if user:
                self.current_user = user
                self.message_handler.login_successful(user['role'], user['name'])
                return self.current_user
            else:
                self.message_handler.invalid_credentials()

    def is_logged_in(self):
        return self.current_user is not None

    def get_current_user_role(self):
        if self.current_user:
            return self.current_user['role']
        return None
    # In AuthSystem class
    def show_all_staff(self):
        users = load_users(self.users_file)
        owner_exists = any(user['role'].capitalize() == "Owner" for user in users)

        if owner_exists:
            staff_members = [user for user in users if user['role'].capitalize() == "Staff"]

            if staff_members:
                self.message_handler.staff_list_header()
                for i, staff in enumerate(staff_members, start=1):
                    self.message_handler.display_staff_member(i, staff)
                self.message_handler.staff_list_footer()
            else:
                self.message_handler.no_staff_members_found()
        else:
            self.message_handler.no_owner_exists()


    def welcome_system(self):
        self.message_handler.welcome_message()       