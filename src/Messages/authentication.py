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
        print(f"{Colors.LIGHT_SKY_BLUE}  Welcome to the Authentication Management System! Please follow the prompts to continue.{Colors.RESET}")

    def no_staff_members_found(self):
        print(f"{Colors.YELLOW}No staff members found.{Colors.RESET}")

    def no_owner_exists(self):
        print(f"{Colors.RED}No owner exists in the system. Only an owner can add staff members.{Colors.RESET}")

    def staff_list_header(self):
        print("\n" + "*" * 60)
        print(f"{Colors.BLUE}** List of All Staff Members **".center(60) + Colors.RESET)
        print("*" * 60)
        print("-" * 115)
        print(f"{Colors.CYAN}{'No.':<5} | {'ID':<15} | {'Name':<20} | {'Email':<25} | {'Phone':<15} | {'Date of Birth':<15} |{Colors.RESET}")
        print("-" * 115)

    def display_staff_member(self, index, staff):
        print(f"{Colors.GREEN}{index:<5} | {staff['id']:<15} | {staff['name']:<20} | {staff['email']:<25} | {staff['phone']:<15} | {staff['date_of_birth']:<15} |{Colors.RESET}")

    def staff_list_footer(self):
        print("-" * 115)

    def invalid_user_id(self):
        print(f"{Colors.RED}Invalid user ID. You are not authorized to log in.{Colors.RESET}")

 