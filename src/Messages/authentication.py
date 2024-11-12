

class AuthHandler:
    
    def email_already_taken(self):
        print("Email already taken! Try again.")

    def owner_exists(self):
        print("An owner already exists! You cannot create another owner.")

    def staff_limit_reached(self):
        print("Staff limit reached! You cannot create more than 10 staff members.")

    def signup_successful(self):
        print("Signup successful!")

    def login_successful(self, role, name):
        print(f"Login successful! Welcome {role} {name}.")

    def invalid_credentials(self):
        print("Invalid email or password. Try again.")

    def user_data_file_not_found(self):
        print("User data file not found, creating a new one.")

    def user_data_read_error(self):
        print("Error reading user data, resetting file.")

    def user_save_error(self, exception):
        print(f"An error occurred while saving users: {exception}")
