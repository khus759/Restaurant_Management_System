from Src.Authentication.auth_system import AuthSystem
from Src.Dashboard.owner_dashboard import OwnerDashboard
from Src.Dashboard.staff_dashboard import StaffDashboard

# Define color codes
class Colors:
    HEADER = "\033[95m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
    BRIGHT_MAGENTA = "\033[95m"
    BG_CYAN = "\033[46m"

def show_dashboard(user_role):
    if user_role == "Owner":
        dashboard = OwnerDashboard()
        dashboard.display_dashboard()
    elif user_role == "Staff":
        dashboard = StaffDashboard()
        dashboard.display_dashboard()
    else:
        print(f"{Colors.RED}Invalid role{Colors.RESET}")

def main():
    auth_system = AuthSystem()
    
    while True:
        print(f"{Colors.BRIGHT_MAGENTA}{'-'*80}")
        print(f"🍕☕👩‍🍳 {Colors.YELLOW}********* Welcome to the Taste of Tradition Restaurant *********{Colors.RESET}🍽️ 🍔🍲🍝")
        print(f"{Colors.BRIGHT_MAGENTA}{'-'*80}{Colors.RESET}")
        auth_system.welcome_system()
        print(f"\n{Colors.GREEN}1. Signup")
        print("2. Login")
        print(f"3. Exit{Colors.RESET}")

        try:
            option = input(f"{Colors.CYAN}Choose an option: {Colors.RESET}")
        except ValueError:
            print(f"{Colors.RED}Please enter valid input{Colors.RESET}")
            continue

        if option == "1":
            auth_system.signup()
        elif option == "2":
            user = auth_system.login()
            if user:
                show_dashboard(user["role"])
        elif option == "3":
            print(f"{Colors.YELLOW}Exiting system. Goodbye!{Colors.RESET}")
            break
        else:
            print(f"{Colors.RED}Invalid option! Please try again.{Colors.RESET}")
