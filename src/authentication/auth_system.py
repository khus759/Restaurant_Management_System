
from src.authentication.file_handler import load_users, save_users
from src.authentication.user_validation import validate_name, validate_username, validate_password, validate_role

class AuthSystem:
    def __init__(self, users_file='src/database/users.json'):
        self.users_file = users_file
        self.current_user = None

    def signup(self):
        users = load_users(self.users_file)

        while True:
            while True:
                name = input("Enter your name: ").strip()
                name_error = validate_name(name)
                if name_error:
                    print(name_error)
                    continue
                break

            while True:
                username = input("Enter a username (6+ characters): ").strip()
                username_error = validate_username(username)
                if username_error:
                    print(username_error)
                    continue
                break

            while True:
                password = input("Enter a password (6+ characters): ").strip()
                password_error = validate_password(password)
                if password_error:
                    print(password_error)
                    continue
                break

            while True:
                role = input("Enter your role (Owner/Staff): ").strip().upper()
                role_error = validate_role(role)
                if role_error:
                    print(role_error)
                    continue

                owner_count = sum(1 for user in users if user['role'].upper() == 'OWNER')
                if role == 'OWNER' and owner_count >= 1:
                    print("An owner already exists! You cannot create another owner.")
                    return

                staff_count = sum(1 for user in users if user['role'].upper() == 'STAFF')
                if role == 'STAFF' and staff_count >= 5:
                    print("Staff limit reached! You cannot create more than 5 staff members.")
                    return
                break

            if any(user['username'] == username for user in users):
                print("Username already taken! Try again.")
                continue


            new_user = {
                'name': name,
                'username': username,
                'password': password,
                'role': role.capitalize()
            }

            users.append(new_user)
            save_users(self.users_file, users)
            print("Signup successful!")
            break

    def login(self):
        users = load_users(self.users_file)
        while True:
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()

            user = next((user for user in users if user['username'] == username and user['password'] == password), None)

            if user:
                self.current_user = user
                print(f"Login successful! Welcome {user['role']} {user['name']}.")
                break
            else:
                print("Invalid username or password. Try again.")

