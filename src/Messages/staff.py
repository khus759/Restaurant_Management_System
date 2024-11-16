
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"
RESET = "\033[0m"

def profile_updated():
    print(f"{BRIGHT_GREEN} ✔️ Profile updated successfully.{RESET}")

def invalid_credentials():
    print(f"{BRIGHT_RED}❌ Invalid credentials.{RESET}")

def employee_added():
    print(f"{BRIGHT_GREEN}✔️ Employee added successfully.{RESET}")

def employee_not_found():
    print(f"{BRIGHT_RED}❌ Employee not found.{RESET}")

def employee_deleted():
    print(f"{BRIGHT_GREEN}✔️ Employee deleted successfully.{RESET}")

def no_employees_found():
    print("No employees found.")

def display_profile(emp):
    print(f"\n{BRIGHT_CYAN}=== Employee Profile ==={RESET}")
    print("--------------------------------")
    print(f"{BRIGHT_MAGENTA}   Personal Information {RESET}")
    print("   --------------------")
    print(f"   Name           : {emp.get('name', 'N/A')}")
    print(f"   Gender         : {emp.get('gender', 'N/A')}")
    print(f"   Date of Birth  : {emp.get('date_of_birth', 'N/A')}")
    print(f"   Email          : {emp.get('email', 'N/A')}")
    print(f"   Phone          : {emp.get('phone', 'N/A')}")
    
    print(f"\n{BRIGHT_MAGENTA}   Job Information {RESET}")
    print("   --------------------")
    print(f"   Role           : {emp.get('role', 'N/A')}")
    print(f"   Designation    : {emp.get('designation', 'N/A')}")
    print(f"   Joining Date   : {emp.get('joining_date', 'N/A')}")
    print(f"   Salary         : {emp.get('salary', 'N/A')}")
    print(f"   Status         : {emp.get('status', 'N/A')}")
    if emp.get('status') == 'inactive':
        print(f"   Resign Date    : {emp.get('resign_date', 'N/A')}")

    print(f"\n{BRIGHT_MAGENTA}   Address Information {RESET}")
    print("   --------------------")
    print(f"   Country        : {emp.get('country', 'N/A')}")
    print(f"   State          : {emp.get('state', 'N/A')}")
    print(f"   District       : {emp.get('district', 'N/A')}")
    print(f"   City/Village   : {emp.get('city_village', 'N/A')}")
    print(f"   Pincode        : {emp.get('pincode', 'N/A')}")
    print("--------------------------------\n")

def display_all_profiles(emp, index):
    print("\n--------------------------------")
    print(f"{BRIGHT_YELLOW}       Employee {index}{RESET}")
    print("--------------------------------")
    display_profile(emp)

def welcome_message():
    print(f"{BRIGHT_BLUE} 😀 Welcome to the Staff Management System! Please follow the prompts to continue.😜{RESET}")

def exit_message():
    print(f"{BRIGHT_BLUE} 😀 Thank you for using the Staff Management System. Goodbye!{RESET}")
