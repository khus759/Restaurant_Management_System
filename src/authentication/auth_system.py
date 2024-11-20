import uuid
import maskpass  # Secure password input
import json  # Required to read/write employee.json
from Src.Authentication.file_operation import load_users, save_users
from Src.Utility.validation import (
    validate_name, validate_email, validate_password,
    validate_phone_number, validate_date_of_birth
)
from Src.Utility.user_input import get_valid_input
from Src.Utility.path_manager import users_file, employee_file
from Src.Messages.authentication import AuthHandler
from Src.Utility.color import Colors

class AuthSystem:
    def __init__(self):
        self.users_file = users_file  # Path for users file
        self.employee_file = employee_file  # Path for employee file (employee.json)
        self.current_user = None
        self.message_handler = AuthHandler()
        self.color = Colors()

    def signup(self):
        # Load current users from employee.json
        try:
            users = load_users(self.users_file)
        except FileNotFoundError:
            users = []

        while True:
            name = get_valid_input(f"{Colors.CYAN}Enter your name: ", validate_name)

            while True:
                email = get_valid_input("Enter your email: ", validate_email).lower()
                if any(user['email'] == email for user in users):
                    print(f"{Colors.RED}This email ID is already taken. Please try a different email.{Colors.RESET}")
                else:
                    break

            while True:
                password = maskpass.askpass("Enter a password (6+ characters): ", mask="*")
                if validate_password(password):
                    break
                print(f"{Colors.RED}Invalid password. Please try again.{Colors.RESET}")

            phone = get_valid_input("Enter your phone number (10 digits): ", validate_phone_number)
            dob = get_valid_input("Enter your date of birth (YYYY-MM-DD): ", validate_date_of_birth)

            # Automatically assign roles: First user is Owner, subsequent users are Staff
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

            # Append to users list and save to file
            users.append(new_user)
            save_users(self.users_file, users)

            # Notify user of successful signup
            self.message_handler.signup_successful()
            break

    def login(self):
        # Load users from employee.json
        try:
            users = load_users(self.users_file)
        except FileNotFoundError:
            users = []

        while True:
            email = get_valid_input("Enter your email: ", validate_email).lower()

            password = maskpass.askpass(f"{Colors.RESET}Enter your password: ", mask="*")

            # Check if the email and password match a user
            user = next((user for user in users if user['email'] == email and user['password'] == password), None)
            
            if user:
                # Check if the user is an "Owner"
                if user['role'].lower() == 'owner':
                    self.current_user = user
                    self.message_handler.login_successful(user['role'], user['name'])
                    return self.current_user
                else:
                    # Match user ID with employee.json for non-owners
                    user_id = user.get('id')
                    if self.is_user_id_valid(user_id):
                        self.current_user = user
                        self.message_handler.login_successful(user['role'], user['name'])
                        return self.current_user
                    else:
                        self.message_handler.invalid_user_id()  # User ID mismatch for non-owner
            else:
                self.message_handler.invalid_credentials()

    def is_user_id_valid(self, user_id):
        # Load employee.json file and check if the user_id is valid
        try:
            with open(self.employee_file, 'r') as f:
                employees = json.load(f)
                return any(emp['id'] == user_id for emp in employees)
        except FileNotFoundError:
            return False

    def is_logged_in(self):
        return self.current_user is not None

    def get_current_user_role(self):
        if self.current_user:
            return self.current_user['role']
        return None

    # Show all staff members for the owner role
    def show_all_staff(self):
        try:
            users = load_users(self.users_file)
        except FileNotFoundError:
            users = []
            
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

    # Display the welcome message
    def welcome_system(self):
        self.message_handler.welcome_message()
