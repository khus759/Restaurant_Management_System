from Src.Utility.color import Colors
class AuthHandler:
    def __init__(self):
        self.color = Colors()

    def email_already_taken(self):
        print(f"{Colors.YELLOW}Email already taken! Try again.{Colors.RESET}")

    def owner_exists(self):
        print(f"{Colors.YELLOW}An owner already exists! You cannot create another owner.{Colors.RESET}")

    def staff_limit_reached(self):
        print(f"{Colors.YELLOW}Staff limit reached! You cannot create more than 10 staff members.{Colors.RESET}")

    def signup_successful(self):
        print(f"{Colors.GREEN}Signup successful!{Colors.RESET}")

    def login_successful(self, role, name):
        print(f"{Colors.GREEN}Login successful! Welcome {role} {name}.{Colors.RESET}")

    def invalid_credentials(self):
        print(f"{Colors.RED}Invalid email or password. Try again.{Colors.RESET}")

    def user_data_file_not_found(self):
        print(f"{Colors.RED}User data file not found, creating a new one.{Colors.RESET}")

    def user_data_read_error(self):
        print(f"{Colors.RED}Error reading user data, resetting file.{Colors.RESET}")

    def user_save_error(self, exception):
        print(f"{Colors.RED}An error occurred while saving users: {exception}{Colors.RESET}")
    
    def welcome_message(self):
        print(f"{Colors.BLUE} 😀 Welcome to the Authentication Management System! Please follow the prompts to continue.😜{Colors.RESET}")
