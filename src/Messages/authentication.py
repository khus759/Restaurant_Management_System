class AuthHandler:

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    def email_already_taken(self):
        print(f"{self.YELLOW}Email already taken! Try again.{self.RESET}")

    def owner_exists(self):
        print(f"{self.YELLOW}An owner already exists! You cannot create another owner.{self.RESET}")

    def staff_limit_reached(self):
        print(f"{self.YELLOW}Staff limit reached! You cannot create more than 10 staff members.{self.RESET}")

    def signup_successful(self):
        print(f"{self.GREEN}Signup successful!{self.RESET}")

    def login_successful(self, role, name):
        print(f"{self.GREEN}Login successful! Welcome {role} {name}.{self.RESET}")

    def invalid_credentials(self):
        print(f"{self.RED}Invalid email or password. Try again.{self.RESET}")

    def user_data_file_not_found(self):
        print(f"{self.RED}User data file not found, creating a new one.{self.RESET}")

    def user_data_read_error(self):
        print(f"{self.RED}Error reading user data, resetting file.{self.RESET}")

    def user_save_error(self, exception):
        print(f"{self.RED}An error occurred while saving users: {exception}{self.RESET}")
