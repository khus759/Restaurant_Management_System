import uuid
import getpass
from Src.Authentication.file_operation import load_users, save_users
from Src.Utility.validation import (
    validate_name, validate_email, validate_password,
    validate_phone_number, validate_role, validate_date_of_birth
)
from Src.Utility.user_input import get_valid_input
from Src.Utility.path_manager import users_file
from Src.Messages.authentication import AuthHandler

class AuthSystem:
    def __init__(self):
        self.users_file = users_file
        self.current_user = None
        self.message_handler = AuthHandler()

    def signup(self):
        users = load_users(self.users_file)

        while True:
            name = get_valid_input("Enter your name: ", validate_name)
            email = get_valid_input("Enter your email: ", validate_email).lower()
            password = getpass.getpass("Enter a password (6+ characters): ", validate_password)
            phone = get_valid_input("Enter your phone number (10 digits): ", validate_phone_number)
            role = get_valid_input("Enter your role (Owner/Staff): ", validate_role)
            dob = get_valid_input("Enter your date of birth (YYYY-MM-DD): ", validate_date_of_birth)

            if any(user['email'] == email for user in users):
                self.message_handler.email_already_taken()
                continue

            owner_count = sum(1 for user in users if user['role'].upper() == 'OWNER')
            if role.upper() == 'OWNER' and owner_count >= 1:
                self.message_handler.owner_exists()
                return

            # staff_count = self.count_roles(users, 'Staff')
            # if role.upper() == 'STAFF' and staff_count >= 10:
            #     self.message_handler.staff_limit_reached()
            #     return

            #name_prefix = name[::2].upper()  
            # user_id = f"{name_prefix}-{str(uuid.uuid4())[:4]}"
            user_id = str(uuid.uuid4()).replace("-", "")[:8].upper()
            new_user = {
                'id': user_id,
                'name': name,
                'email': email,
                'password': password,
                'phone': phone,
                 'role': role.capitalize(),
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
            password = getpass.getpass("Enter your password: ")

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
    
    def show_all_staff(self):
        users = load_users(self.users_file)
        owner_exists = any(user['role'].capitalize() == "Owner" for user in users)

        if owner_exists:
            staff_members = [user for user in users if user['role'].capitalize() == "Staff"]
            
            if staff_members:
                print("\n" + "*" * 60)
                print("**** List of All Staff Members ****".center(60))
                print("*" * 60)
                print("-" * 115)
                print(f"{'No.':<5} | {'ID':<15} | {'Name':<20} | {'Email':<25} | {'Phone':<15} | {'Date of Birth':<15} |")
                print("-" * 115)
                for i, staff in enumerate(staff_members, start=1):
                    print(f"{i:<5} | {staff['id']:<15} | {staff['name']:<20} | {staff['email']:<25} | {staff['phone']:<15} | {staff['date_of_birth']:<15} |")
                print("-" * 115)
            else:
                print("No staff members found.")
        else:
            print("No owner exists in the system. Only an owner can add staff members.")